from django.forms import ModelForm
from . models import Place_details

class PlaceForm(ModelForm):
    class Meta:
        model = Place_details
        fields = '__all__'                  # ['place','summery','year']