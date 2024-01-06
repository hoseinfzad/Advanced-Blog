from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView

# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['message'] = 'Hello World!'
        return context