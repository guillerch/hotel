from django.contrib import admin
from .models import Room

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    '''Admin View for Room'''

    list_display = ('type','price')
    list_filter = ('type','price')
    readonly_fields = ('created_at','updated_at')
    search_fields = ('type','price')
    ordering = ('type','price')