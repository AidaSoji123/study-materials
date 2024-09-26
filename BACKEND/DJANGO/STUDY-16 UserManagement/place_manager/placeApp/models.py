from django.db import models

# Create your models here.
class WebInfo(models.Model):
    rating =models.CharField(max_length=10,null=True)
    cirtified_by = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.rating

class Founder(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "founder_tb"
        
class Traveller(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "traveller_tb"
        

    
class Place_details(models.Model):
    place = models.CharField(max_length=100)
    summery = models.CharField(max_length=100)
    year = models.IntegerField(default=2024)
    image = models.ImageField(upload_to='images/' ,null=True)
    web_details = models.OneToOneField(WebInfo,on_delete=models.SET_NULL,related_name='place',null=True)
    
    founted_by = models.ForeignKey(Founder,null=True,on_delete=models.CASCADE,related_name='founted')
    
    travellers = models.ManyToManyField(Traveller,related_name='visited')
    def __str__(self):
        return self.place
    
    class Meta:
         db_table = "place_details_tb"
    
