from django.contrib import admin
from django.urls import path
from clarim_api import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('registration/',views.Teste.as_view(),name='teste'),
    path('login/',obtain_auth_token,name='get_token'),
]
