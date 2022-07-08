from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Reservation
import json

class ReservationView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            reservation = list(Reservation.objects.filter(id=id).values())
            if len(reservation) > 0:
                reservations = reservation[0]
                data = {'message': "Success", 'Reservation': reservations}
            else:
                data = {'message': "Reservation not found..."}
            return JsonResponse(data)
        else:
            reservation = list(Reservation.objects.values())
            if len(reservation) > 0:
                data = {'message': "Success", 'Reservation': reservation}
            else:
                data = {'message': "reservation not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Reservation.objects.create(
            room=jd['room'],
            guest=jd['guest'],
            status=jd['status'],
            reservation_date=jd['reservation_date'],
            checkin=jd['checkin'],
            checkout=jd['checkout']
            )
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        reservations = list(Reservation.objects.filter(id=id).values())
        if len(reservations) > 0:
            reservation = Reservation.objects.get(id=id)
            reservation.room = jd['room']
            reservation.guest = jd['guest']
            reservation.status = jd['status']
            reservation.reservation_date=jd['reservation_date']
            reservation.checkin=jd['checkin']
            reservation.checkout=jd['checkout']
            reservation.save()
            data = {'message': "Success"}
        else:
            data = {'message': "reservation not found..."}
        return JsonResponse(data)

    def delete(self, request, id):
        reservations = list(Reservation.objects.filter(id=id).values())
        if len(reservations) > 0:
            Reservation.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Reservation not found..."}
        return JsonResponse(data)