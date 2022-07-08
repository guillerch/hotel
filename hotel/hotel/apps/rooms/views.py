from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Room
import json

# Create your views here.

class RoomView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            room = list(Room.objects.filter(id=id).values())
            if len(room) > 0:
                rooms = room[0]
                data = {'message': "Success", 'Room': rooms}
            else:
                data = {'message': "Room not found..."}
            return JsonResponse(data)
        else:
            room = list(Room.objects.values())
            if len(room) > 0:
                data = {'message': "Success", 'Room': room}
            else:
                data = {'message': "Room not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Room.objects.create(type=jd['type'], description=jd['description'], price=jd['price'])
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        rooms = list(Room.objects.filter(id=id).values())
        if len(rooms) > 0:
            room = Room.objects.get(id=id)
            room.type = jd['type']
            room.description = jd['description']
            room.price = jd['price']
            room.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Room not found..."}
        return JsonResponse(data)

    def delete(self, request, id):
        rooms = list(Room.objects.filter(id=id).values())
        if len(rooms) > 0:
            Room.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Room not found..."}
        return JsonResponse(data)