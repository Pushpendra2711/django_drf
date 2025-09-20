import json

from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from apis import models

# Create your View here.


@method_decorator(csrf_exempt, name="dispatch")
class NormalView(View):
    def get(self, request, id):
        print(f"id {id} and type of the id is {type(id)}")
        data = models.NormalModel.objects.get(user_id=id)
        dic = {"usr_id": data.user_id, "name": data.name, "age": data.age}
        return JsonResponse(dic)
        # return HttpResponse("hello")

    def post(self, request):
        data = json.loads(request.body)
        print(data)
        user_id = data.get("user_id")
        name = data.get("name")
        age = data.get("age")
        x = models.NormalModel(user_id=user_id, name=name, age=age)
        x.save()
        return HttpResponse("data successfully created")
