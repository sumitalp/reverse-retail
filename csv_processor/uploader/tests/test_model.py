from factory import Faker
import pytest

from django.db.utils import IntegrityError
from csv_processor.uploader.models import Address, Customer
from csv_processor.uploader.tests.factories import AddressFactory, CustomerFactory


class TestUploaderModels:
    def test_customer_with_integrityerror(self, customer):
        with pytest.raises(IntegrityError) as iexc:
            customer_1 = Customer.objects.create(
                name=customer.name, first_name=customer.first_name, email=customer.email
            )
            assert (
                'duplicate key value violates unique constraint "name_email_idx"'
                in iexc
            )

    def test_address_without_payload(self):
        with pytest.raises(IntegrityError) as iexc:
            Address.objects.create()
            assert (
                'null value in column "customer_id" violates not-null constraint'
                in iexc
            )

    def test_address_model(self, customer):
        address, create = Address.objects.get_or_create(
            street=Faker("name"),
            city=Faker("city"),
            country=Faker("country"),
            zipcode=Faker("zipcode"),
            customer=customer,
        )
        assert create

    def test_customer_address(self):
        customer_1, customer_2, customer_3 = CustomerFactory.create_batch(size=3)
        result_1 = AddressFactory.create_batch(size=2, customer=customer_1)
        AddressFactory.create_batch(size=2, customer=customer_2)
        AddressFactory.create_batch(size=1, customer=customer_3)

        assert result_1[0].customer == customer_1
        assert customer_2.addresses.count() == 2
