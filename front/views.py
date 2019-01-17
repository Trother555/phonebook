from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from api.forms import PersonForm
from django.urls import reverse_lazy
import requests as rq
import json

api_endpoint = 'http://localhost:8000/api/v1/person/'


class CreatePersonView(FormView):
    template_name = 'front/create.html'
    form_class = PersonForm
    success_url = reverse_lazy('front:get')

    def form_valid(self, form):
        form.cleaned_data['phone_number'] = str(
            form.cleaned_data['phone_number'])
        rq.post(api_endpoint, json=form.cleaned_data)
        return super().form_invalid(form)


class GetPersonView(TemplateView):
    template_name = 'front/get.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if ('first_name' in self.request.GET and
                'last_name' in self.request.GET):
            first_name = self.request.GET['first_name']
            last_name = self.request.GET['last_name']
            res = rq.get(api_endpoint, params={
                'first_name': first_name, 'last_name': last_name})
            if res.status_code == 200:
                res = json.loads(res.content)["objects"]
                if len(res) > 0:
                    context['person'] = res[0]
                else:
                    context['not_found'] = True
        return context
