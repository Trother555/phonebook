from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.validation import FormValidation
from api.models import Person
from api.forms import PersonForm


class PersonResource(ModelResource):
    class Meta:
        queryset = Person.objects.all()
        resource_name = 'person'
        authorization = Authorization()
        fields = ['first_name', 'last_name', 'phone_number']
        filtering = {
            "first_name": ('exact'),
            "last_name": ('exact'),
        }
        validation = FormValidation(form_class=PersonForm)
