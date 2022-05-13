import factory
from factory import fuzzy
from django.utils import timezone

from csv_processor.uploader.models import Address, Customer


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    name = factory.Faker("name")
    first_name = factory.Faker("first_name")
    created = fuzzy.FuzzyDateTime(timezone.now())


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    customer = factory.SubFactory(CustomerFactory)
    street = factory.Faker("name")
    city = factory.Faker("city")
    country = factory.Faker("country")
    zipcode = factory.Faker("zipcode")
