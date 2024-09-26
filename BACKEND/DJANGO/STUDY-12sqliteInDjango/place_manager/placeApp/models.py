from django.db import models

# Create your models here.
class Place_details(models.Model):
    place = models.CharField(max_length=100)
    summery = models.CharField(max_length=100)
    year = models.IntegerField(default=2024)
    image = models.ImageField(upload_to='images/' ,null=True)
     
    def __str__(self):
        return self.place
    
    class Meta:
         db_table = "place_details_tb"
    
class Founder(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "founder_tb"