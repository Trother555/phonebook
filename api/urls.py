from tastypie.api import Api
from api.resources import PersonResource


api = Api(api_name='v1')
api.register(PersonResource())

urlpatterns = api.urls
