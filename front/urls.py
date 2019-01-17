from django.urls import path
from front import views

app_name = 'front'
urlpatterns = [
    path('create',
         views.CreatePersonView.as_view(),
         name='create'),
    path('get',
         views.GetPersonView.as_view(),
         name='get'),
]
