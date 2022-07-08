from django.db import models
from apps.users.models import Customer
from apps.rooms.models import Room
from shortuuidfield import ShortUUIDField
# Create your models here.

class Reservation(models.Model):
    class ReservationType(models.TextChoices):
        pending = 'Pendiente'
        paid = 'Pagado'
        deleted = 'Eliminado'

    uuid = ShortUUIDField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Habitación', null=False)
    guest = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='ID cliente', null=False)
    status = models.CharField('Estado', max_length=10, choices=ReservationType.choices, default=ReservationType.pending)
    reservation_date = models.DateTimeField('Día de reservación', auto_now=False, auto_now_add=True, blank=False, null=False)
    checkin = models.DateField('Ingreso', auto_now=False, auto_now_add=False, blank=False, null=False)
    checkout = models.DateField('Salida', auto_now=False, auto_now_add=False, blank=False, null=False)
    created_at=models.DateTimeField('Creado',auto_now_add=True)
    updated_at=models.DateTimeField('Ultima edición',auto_now=True)

    class Meta:
        verbose_name='Reservación'
        verbose_name_plural='Reservaciones'

    def __str__(self):
        return f'{self.guest} - {self.uuid}'

    def days_total(self):
        total = (self.checkout - self.checkin).days
        return total

    def get_days(self):
        diff = self.days_total()
        if diff <=0:
            return 1
        else:
            return diff