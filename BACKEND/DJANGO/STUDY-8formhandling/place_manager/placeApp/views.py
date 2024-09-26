from django.shortcuts import render

# Create your views here.
def create(request):
    if request.POST:
      print(request.POST)
      print(request.POST.get('place'))
      print(request.POST.get('summery'))
    return render(request, 'create.html')

def list(request):
    
    person ={"data": [{
        "name" : "silvi",
        "age" : 20,
        "gender" : "female",
        "email" : "aida@gmail.com",
        "address": {
            "city" : "Dhaka",
            "country" : "Bangladesh",
            "house" : "kelamkunnel",
                   },
        "phone": 9784667474,
         "image":"img.webp",
    
    },
              {
        "name" : "amala",
        "age" : 20,
        "gender" : "female",
        "email" : "aida@gmail.com",
        
        "phone": 9784667474,
         "image":"img.webp",
    
    },
              {
        "name" : "Anoop",
        "age" : 20,
        "gender" : "male",
        "email" : "anoop@gmail.com",
        "address": {
            "city" : "Dhaka",
            "country" : "Bangladesh",
            "house" : "kelamkunnel",
           
            },
        "phone": 9784667474,
          "image":"img.webp",
    
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
    return render(request,"list.html",person)    

def edit(request):
    return render(request, 'edit.html')
