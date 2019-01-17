from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()

    def __str__(self):
        return f'{self.last_name} {self.first_name} - {self.phone_number}'

    class Meta:
        unique_together = ('first_name', 'last_name')
