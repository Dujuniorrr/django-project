from django.db import models

# Create your models here.
class Field(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    description = models.CharField(max_length=150, verbose_name='Descrição')
    
    def __str__(self):
        return "{} ({})".format(self.name, self.description)

class Activity(models.Model):
    number = models.IntegerField(verbose_name="Número")
    points = models.DecimalField(verbose_name="Pontos", decimal_places=1, max_digits=4)
    details = models.CharField(max_length=100, verbose_name="Detalhes")
    description = models.CharField(max_length=150, verbose_name='Descrição')
    field = models.ForeignKey(Field, on_delete= models.PROTECT, verbose_name='Campo')
    
    def __str__(self):
        return "{} - {} ({})".format(self.number, self.description, self.field.name)