from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.
class Profile(models.Model):
    complet_name = models.CharField(max_length=100, verbose_name='Nome Completo',  null=True)
    cpf = models.CharField(max_length=14, validators=[MinLengthValidator(14)], verbose_name='CPF',  null=True)
    phone =  models.CharField(max_length=16, validators=[MinLengthValidator(14)],verbose_name='Telefone',  null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{} - ({})".format(self.complet_name, self.cpf)
    