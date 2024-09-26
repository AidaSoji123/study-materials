from django.shortcuts import render, redirect, get_object_or_404
from .models import Place_details
from .forms import PlaceForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        frm = PlaceForm(request.POST, request.FILES)  # Handle file uploads
        if frm.is_valid():
            frm.save()
            return redirect('list')  # Redirect after successful form submission
    else:
        frm = PlaceForm()
    return render(request, 'create.html', {'frm': frm})

def list(request):
    place_data = Place_details.objects.filter(year=2021)
    return render(request, "list.html", {"data": place_data})

def edit(request, pk):
    instance_to_be_edited = get_object_or_404(Place_details, pk=pk)
    if request.method == 'POST':
        frm = PlaceForm(request.POST, request.FILES, instance=instance_to_be_edited)  # Handle file uploads
        if frm.is_valid():
            frm.save()
            return redirect('list')  # Redirect after successful form submission
    else:
        frm = PlaceForm(instance=instance_to_be_edited)
    return render(request, 'create.html', {'frm': frm})

def delete(request, pk):
    instance = get_object_or_404(Place_details, pk=pk)
    instance.delete()
    return redirect('list')  # Redirect after deletion
