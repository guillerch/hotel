from django.contrib import admin
from .models import Reservation
# Register your models here.

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    '''Admin View for Reservation'''

    list_display = ('guest','room','status','reservation_date','uuid')
    list_filter = ('guest','room','status','reservation_date')
    readonly_fields = ('created_at','updated_at')
    search_fields = ('guest','room','status','reservation_date')
    ordering = ('guest','room','status','reservation_date')