from django.shortcuts import render, redirect, get_object_or_404
from .models import Place_details
from .forms import PlaceForm
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='users/login/')
def list(request):
    print(request.COOKIES)
    visits = int(request.COOKIES.get('visits',0))
    visits = visits + 1
    place_data = Place_details.objects.filter(year=2021)
    response = render(request, "list.html", {"data": place_data,'visits':visits})
    response.set_cookie('visits',visits)
    return response

@login_required(login_url='users/login/')
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

@login_required(login_url='users/login/')
def delete(request, pk):
    instance = get_object_or_404(Place_details, pk=pk)
    instance.delete()
    return redirect('list')  # Redirect after deletion
