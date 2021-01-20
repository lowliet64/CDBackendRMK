from django.contrib import admin
from django.urls import path,include
from clarim_api import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'artigos', views.ArtigoViewSet)


urlpatterns = [
    path('registration/',views.Teste.as_view(),name='teste'),
    path('login/',obtain_auth_token,name='get_token'),
    path('api/v1/',include(router.urls)),
]
