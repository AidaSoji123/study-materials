from django.shortcuts import render
from . models import Place_details
from . forms import PlaceForm
# Create your views here.

def create(request):
    if request.POST:
      frm = PlaceForm(request.POST)
      if frm.is_valid():
        frm.save()
    else:
      frm = PlaceForm()       
    return render(request, 'create.html',{'frm':frm})

def list(request):
  place_data = Place_details.objects.all()
  print(place_data)
  return render(request,"list.html",{"data":place_data})    

def edit(request,pk):
  instance_to_be_edited = Place_details.objects.get(pk=pk)
  if request.POST:
    frm = PlaceForm(request.POST,instance=instance_to_be_edited)
    if frm.is_valid():
        frm.save()
  else:
    frm = PlaceForm(instance=instance_to_be_edited)
  return render(request, 'create.html',{ 'frm':frm })

def delete(request,pk):
  instance = Place_details.objects.get(pk=pk)
  instance.delete()
  place_data = Place_details.objects.all()
  return render(request,"list.html",{"data":place_data})    