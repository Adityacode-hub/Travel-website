from django.db import models

class Public(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=255)
    email=models.CharField(max_length=122,unique=True)
    password= models.CharField(max_length=50,blank=True,null=True)
    def __str__(self):
        return(self.username)
    
