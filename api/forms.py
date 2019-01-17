from django.forms import ModelForm
from api.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone_number']
