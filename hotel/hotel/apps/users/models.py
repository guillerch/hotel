from django.db import models
# Create your models here.

class Customer(models.Model):
    first_name = models.CharField('Nombres',max_length=255,blank=False)
    last_name = models.CharField('Apellidos',max_length=255,blank=False)
    phone=models.CharField('Télefono',max_length=20,blank=True,null=True)
    email = models.EmailField('Correo',max_length=255,unique=True)
    created_at=models.DateTimeField('Creado',auto_now_add=True)
    updated_at=models.DateTimeField('Ultima edición',auto_now=True)

    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'