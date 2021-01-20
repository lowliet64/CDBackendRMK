from django.shortcuts import render
from django.views.generic import View
from rest_framework import viewsets
from rest_framework import permissions
from clarim_api.models import Artigo,CustomUser
from clarim_api.serializers import ArtigoSerializer
# Create your views here.


class Teste (View):
    template_name='clarim_api/teste.html'
    def get(self,request):
        return render(request,self.template_name)


class ArtigoViewSet(viewsets.ModelViewSet):
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


