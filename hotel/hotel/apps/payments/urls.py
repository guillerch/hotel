from django.urls import path
from .views import PaymentView

urlpatterns = [
    path('customers/', PaymentView.as_view()),
]