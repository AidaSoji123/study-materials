from django.contrib import admin
from . models import Place_details,Founder,WebInfo,Traveller

# Register your models here.
admin.site.register(Place_details)
admin.site.register(Founder)
admin.site.register(WebInfo)
admin.site.register(Traveller)