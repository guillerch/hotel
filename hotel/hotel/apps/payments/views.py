from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Payment
import json

# Create your views here.
class PaymentView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            payment = list(Payment.objects.filter(id=id).values())
            if len(payment) > 0:
                payments = payment[0]
                data = {'message': "Success", 'Payment': payments}
            else:
                data = {'message': "Payment not found..."}
            return JsonResponse(data)
        else:
            payment = list(Payment.objects.values())
            if len(payment) > 0:
                data = {'message': "Success", 'Payment': payment}
            else:
                data = {'message': "Payment not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Payment.objects.create(
            reservations=jd['reservations'],
            guest=jd['guest'],
            pay_method=jd['pay_method'],
            total=jd['total'],
            payment_date=jd['payment_date']
            )
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        payments = list(Payment.objects.filter(id=id).values())
        if len(payments) > 0:
            payment = Payment.objects.get(id=id)
            payment.reservations = jd['reservations']
            payment.guest = jd['guest']
            payment.pay_method = jd['pay_method']
            payment.total=jd['total']
            payment.payment_date=jd['payment_date']
            payment.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Payment not found..."}
        return JsonResponse(data)

    def delete(self, request, id):
        payments = list(Payment.objects.filter(id=id).values())
        if len(payments) > 0:
            Payment.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Payment not found..."}
        return JsonResponse(data)