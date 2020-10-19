
from django.db import models 
from django.db.models import Model 
# Create your models here. 
  
class contact(models.Model): 
    name = models.CharField(max_length = 200) 
    email = models.EmailField(max_length=200) 
    address = models.CharField(max_length = 200) 
    message = models.CharField(max_length = 200) 

    def __str__(self):
        return self.name