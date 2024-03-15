from django.shortcuts import render
from django.views.generic import TemplateView


class index(TemplateView):
  

    def get(self,request,*args, **kwargs):
        return render(request, 'deshboard/index.html')

