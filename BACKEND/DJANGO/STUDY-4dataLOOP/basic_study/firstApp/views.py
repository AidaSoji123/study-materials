from django.http import  HttpResponse
from django.shortcuts import render

# Create your views here.
def greeting(request):
    return HttpResponse("Hellooooo Mayaavii...")

def htmlpage(request):
    # in views key is considered as variable to template so must take the list as a value of data keyword
    person ={"data": [{
        "name" : "silvi",
        "age" : 20,
        "gender" : "female",
        "email" : "aida@gmail.com",
        "address": {
            "city" : "Dhaka",
            "country" : "Bangladesh",
            "house" : "kelamkunnel"
        },
        "phone": 9784667474,
    
    },
              {
        "name" : "amala",
        "age" : 20,
        "gender" : "female",
        "email" : "aida@gmail.com",
        
        "phone": 9784667474,
    
    },
              {
        "name" : "Anoop",
        "age" : 20,
        "gender" : "male",
        "email" : "anoop@gmail.com",
        "address": {
            "city" : "Dhaka",
            "country" : "Bangladesh",
            "house" : "kelamkunnel"
        },
        "phone": 9784667474,
    
    },
      {
        "name" : "Mayaavii",
        "age" : 20,
        "gender" : "female",
        "email" : "aida@gmail.com",
        "address": {
            "city" : "Dhaka",
            "country" : "Bangladesh",
            "house" : "kelamkunnel"
        },
        "phone": 9784667474,
    
    },
      {
        "name" : "Mayaavii",
        "age" : 20,
        "gender" : "female",
        "email" : "aida@gmail.com",
        "address": {
            "city" : "Dhaka",
            "country" : "Bangladesh",
            "house" : "kelamkunnel"
        },
        "phone": 9784667474,
    
    },
      {
        "name" : "Mayaavii",
        "age" : 20,
        "gender" : "female",
        "email" : "aida@gmail.com",
        "address": {
            "city" : "Dhaka",
            "country" : "Bangladesh",
            "house" : "kelamkunnel"
        },
        "phone": 9784667474,
    
    },
      {
        "name" : "Mayaavii",
        "age" : 20,
        "gender" : "female",
        "email" : "aida@gmail.com",
        "address": {
            "city" : "Dhaka",
            "country" : "Bangladesh",
            "house" : "kelamkunnel"
        },
        "phone": 9784667474,
    
    },
      {
        "name" : "Mayaavii",
        "age" : 20,
        "gender" : "female",
        "email" : "aida@gmail.com",
        "address": {
            "city" : "Dhaka",
            "country" : "Bangladesh",
            "house" : "santhwanam"
        },
        "phone": 9784667233,
    
    },
      {
        "name" : "Dhaya",
        "age" : 19,
        "gender" : "female",
        "email" : "dhaya@gmail.com",
        "address": {
            "city" : "Dhamascus",
            "country" : "Israel",
            "house" : "kuruvi"
        },
        "phone": 9784667675,
    
    },
      {
        "name" : "Vinu",
        "age" : 30,
        "gender" : "male",
        "email" : "vinu@gmail.com",
        "address": {
            "city" : "Dhaka",
            "country" : "india",
            "house" : "palakkattuchira"
        },
        "phone": 9784667451,
    
    },
      {
        "name" : "anu",
        "age" : 29,
        "gender" : "female",
        "email" : "anu@gmail.com",
        "address": {
            "city" : "Dhaka",
            "country" : "Bangladesh",
            "house" : "kinara"
        },
        "phone": 9784667474,
    
    },
      
              ]
    }
    
    
    array1 = ["a","f","d","gh"]
    context ={
        "person":person,
        "array1":array1,
    }
    return render(request,"index.html",context)    #person pass to the client through our template from server