from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.


class CustomUser(AbstractUser):
    pass




class Artigo(models.Model):
    titulo = models.CharField(max_length=256)
    subtitulo = models.CharField(max_length=256)
    autor = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    tags = models.TextField(blank=True,null=True)
    conteudo = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()




@receiver(post_save,sender = settings.AUTH_USER_MODEL)
def create_auth_token (sender ,instance=None, created =False, **kwargs):
    if(created):
        Token.objects.create(user=instance)