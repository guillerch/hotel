from django.contrib import admin
from .models import Payment
# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    '''Admin View for Payment'''

    list_display = ('guest','reservations','pay_method','total')
    list_filter = ('guest','reservations','pay_method','total')
    readonly_fields = ('created_at','updated_at')
    search_fields = ('guest','reservations','pay_method','total')
    ordering = ('guest','reservations','pay_method','total')