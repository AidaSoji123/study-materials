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

def edit(request):
  return render(request, 'edit.html')
