from django.db import models

# Create your models here.
class Place_details(models.Model):
    place = models.CharField(max_length=100)
    summery = models.CharField(max_length=100)
    year = models.IntegerField(default=2024)
    
    
    def __str__(self):
        return self.place
    
class Founder(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
