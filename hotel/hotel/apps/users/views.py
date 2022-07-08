from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Customer
import json

# Create your views here.

class CustomerView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            client = list(Customer.objects.filter(id=id).values())
            if len(client) > 0:
                clients = client[0]
                data = {'message': "Success", 'customer': clients}
            else:
                data = {'message': "customer not found..."}
            return JsonResponse(data)
        else:
            client = list(Customer.objects.values())
            if len(client) > 0:
                data = {'message': "Success", 'customer': client}
            else:
                data = {'message': "customer not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Customer.objects.create(first_name=jd['first_name'], last_name=jd['last_name'], phone=jd['phone'], email=jd['email'])
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        clients = list(Customer.objects.filter(id=id).values())
        if len(clients) > 0:
            client = Customer.objects.get(id=id)
            client.first_name = jd['first_name']
            client.last_name = jd['last_name']
            client.phone = jd['phone']
            client.email = jd['email']
            client.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Customer not found..."}
        return JsonResponse(data)

    def delete(self, request, id):
        clients = list(Customer.objects.filter(id=id).values())
        if len(clients) > 0:
            Customer.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Customer not found..."}
        return JsonResponse(data)