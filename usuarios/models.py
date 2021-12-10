from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save

# QUI PODE SER ON DEVE CADASTRAR USUARIOS, PODE SER DIRETORES
class  Perfil_do_usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.IntegerField(null=True, blank=True)
    endereco_completo = models.CharField(max_length=500, blank=True, null=True)
    idade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Perfil_do_usuario.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

