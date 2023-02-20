from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Field(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    description = models.CharField(max_length=150, verbose_name='Descrição')
    
    def __str__(self):
        return "{} ({})".format(self.name, self.description)
    
    class Meta:
        verbose_name = 'Campo'
        ordering = ['name']

class Activity(models.Model):
    number = models.IntegerField(verbose_name="Número", unique=True)
    points = models.DecimalField(verbose_name="Pontos", decimal_places=1, max_digits=4)
    details = models.CharField(max_length=100, verbose_name="Detalhes")
    description = models.CharField(max_length=150, verbose_name='Descrição')
    field = models.ForeignKey(Field, on_delete= models.PROTECT, verbose_name='Campo')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuário")
    
    def __str__(self):
        return "{} - {} ({})".format(self.number, self.description, self.field.name)
    
    class Meta:
        verbose_name = 'Atividade'
        ordering = ['number']
        
# class Receipt(models.Model):
#     quantity = models.DecimalField(verbose_name="Quantidade", decimal_places=1, max_digits=4)
#     date = models.DateField(verbose_name="Data")
#     activity = models.ForeignKey(Activity, on_delete=models.PROTECT, verbose_name="Atividade")
    
# class Validation(models.Model):
    
    