from django.db import models
from apps.users.models import Customer
from apps.reservation.models import Reservation
from shortuuidfield import ShortUUIDField
# Create your models here.

class Payment(models.Model):
    class PaymentType(models.TextChoices):
        ccard = 'tarjeta'
        cash = 'efectivo'
        qr = 'qr'

    uuid = ShortUUIDField()
    reservations = models.ForeignKey(Reservation, on_delete=models.CASCADE, verbose_name='Reservación', null=False)
    guest = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='ID cliente', null=False)
    pay_method = models.CharField('Estado', max_length=10, choices=PaymentType.choices, default=PaymentType.ccard)
    total = models.DecimalField('Total', max_digits=10, decimal_places=2, null=False)
    payment_date = models.DateField('Día del pago', auto_now=False, auto_now_add=True, blank=False, null=False)
    created_at=models.DateTimeField('Creado',auto_now_add=True)
    updated_at=models.DateTimeField('Ultima edición',auto_now=True)

    class Meta:
        verbose_name='Pago'
        verbose_name_plural='Pagos'

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