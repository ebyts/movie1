from django.db import models

# Create your models here.

class Movie(models.Model):
    name=models.CharField(max_length=200)
    director=models.CharField(max_length=50)
    year=models.IntegerField()
    desc=models.TextField(max_length=400)
    img=models.ImageField(upload_to='gallry')

    def __str__(self):
        return self.name
    
