from django.db.models import CASCADE
from django.db import models
from model_utils.models import TimeStampedModel


class Customer(TimeStampedModel):
    name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    bank_account_no = models.CharField(max_length=128, blank=True)
    bank_name = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=128, blank=True)
    email = models.EmailField(max_length=128, blank=True)

    class Meta:
        ordering = ("-created",)
        # Unique constraint
        constraints = [
            models.UniqueConstraint(
                fields=["name", "first_name", "email"], name="name_email_idx"
            )
        ]

    def __str__(self) -> str:
        return f"{self.name} {self.first_name}"


class Address(TimeStampedModel):
    # One to Many relations
    customer = models.ForeignKey(Customer, related_name="addresses", on_delete=CASCADE)
    street = models.CharField(max_length=128)
    zipcode = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=128)

    class Meta:
        ordering = ("-created",)

    def __str__(self) -> str:
        return f"Address of {self.customer}"
