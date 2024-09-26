from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def greeting(request):
    return HttpResponse("Hellooooo Mayaavii...")


def dataTransfer(request):
    person = {
        "name": "Mayaavii",
        "age": 20,
        "gender": "female",
        "email": "abc@gmail.com",
        "phone": 9784667474,
        "address": {"city": "Dhaka", "country": "Bangladesh", "house": "kelamkunnel"},
    }
    return render(request, "index.html", person)
