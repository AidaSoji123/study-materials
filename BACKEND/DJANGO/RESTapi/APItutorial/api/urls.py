from django.urls import path
from master.views import index

urlpatterns = [
    path('index/', index, name='index'),
]