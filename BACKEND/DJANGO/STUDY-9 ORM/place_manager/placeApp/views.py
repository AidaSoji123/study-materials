from django.shortcuts import render
from . models import Place_details

# Create your views here.
def create(request):
    if request.POST:
      place = (request.POST.get('place'))
      summery = (request.POST.get('summery'))
      year = (request.POST.get('year'))
      obj = Place_details(place = place,summery = summery,year = year)
      obj.save() 
    return render(request, 'create.html')

def list(request):
  place_data = Place_details.objects.all()
  print(place_data)
  return render(request,"list.html",{"data":place_data})    

def edit(request):
  return render(request, 'edit.html')
