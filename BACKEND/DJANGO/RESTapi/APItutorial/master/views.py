from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Person

from .serializer import PersonSerializer
# Create your views here.

@api_view(['GET','POST','PUT']) 
def index(request):
    if request.method == 'GET':
    
        people_detail = {
            'name': "Anagha",
            'Age' :29,
            'Gender' : "Female",
            'Profession' : "Student",
            'Hobbies' : "Reading",

            }
        return Response(people_detail)
    elif request.method == 'POST':
        return Response('THIS IS A POST METHOD')
        
    elif request.method == 'PUT':
        return Response('THIS IS A PUT METHOD')
        
  # people.objects.all() =>[1,2,3,.....](quaryset) -> JSON -->serializers
 
@api_view(['GET','POST','PUT','PATCH','DELETE']) 
def person(request):
    if request.method == 'GET':
        objPerson = Person.objects.all()
        serializer = PersonSerializer(objPerson, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PersonSerializer{obj, data = data, partial = False}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        
        
        