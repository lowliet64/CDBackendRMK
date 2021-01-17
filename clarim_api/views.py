from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class Teste (View):
    template_name='clarim_api/teste.html'
    def get(self,request):
        return render(request,self.template_name)