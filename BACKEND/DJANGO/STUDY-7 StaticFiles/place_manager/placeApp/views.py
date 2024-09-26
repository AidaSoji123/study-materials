from django.shortcuts import render

# Create your views here.
def create(request):
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
         "image":"https://t4.ftcdn.net/jpg/05/49/86/39/360_F_549863991_6yPKI08MG7JiZX83tMHlhDtd6XLFAMce.jpg",
    
    },
              {
        "name" : "amala",
        "age" : 20,
        "gender" : "female",
        "email" : "aida@gmail.com",
        
        "phone": 9784667474,
         "image":"/static/images/img.webp",
    
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
          "image":"/static/images/img.webp",
    
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
     "image":"/static/images/img.webp",
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
     "image":"/static/images/img.webp",
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
     "image":"/static/images/img.webp",
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
     "image":"/static/images/img.webp",
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
     "image":"/static/images/img.webp",
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
     "image":"/static/images/img.webp",
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
     "image":"/static/images/img.webp",
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
     "image":"/static/images/img.webp",
    },
      
              ]
    }
    return render(request,"list.html",person)    

def edit(request):
    return render(request, 'edit.html')
