from django.db import models

# Create your models here.

class Room(models.Model):
    class RoomType(models.TextChoices):
        simple = 'Simple'
        matrimonial = 'Doble'
        suite = 'Suite'

    type = models.CharField('Tipo de habitación', max_length=10, choices=RoomType.choices, null=False)
    description = models.TextField('Detalles', blank=False, null=False)
    price = models.PositiveIntegerField('Precio por noche',default=10)
    created_at=models.DateTimeField('Creado',auto_now_add=True)
    updated_at=models.DateTimeField('Ultima edición',auto_now=True)

    class Meta:
        verbose_name='Habitación'
        verbose_name_plural='Habitaciones'

    def __str__(self):
        return f'{self.type}'