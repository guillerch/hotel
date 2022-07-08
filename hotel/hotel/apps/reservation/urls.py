from django.urls import path
from .views import ReservationView

urlpatterns = [
    path('reservations/', ReservationView.as_view()),
]