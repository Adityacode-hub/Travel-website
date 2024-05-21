from django.db import models

# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)


class Contact(models.Model):
    name=models.CharField(max_length=155,unique=True)
    phone=models.CharField(max_length=12,null=False)
    email=models.CharField(max_length=122,unique=True)
    date=models.DateField(auto_now=True)
   

    def __str__(self):
        return self.name
