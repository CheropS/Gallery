from django.db import models


# Create your models here.

class Category(models.Model):
    category=models.CharField(max_length=20)
    

    def __str__(self):
        return self.category

class Location(models.Model):
    location=models.CharField(max_length=30)

    def __str__(self):
        return self.location
        
class Image(models.Model):
    image_id=models.ImageField(null=False, blank=False)
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=500)
    location=models.ForeignKey(Location, on_delete=models.CASCADE)
    category=models.ManyToManyField(Category)

    def __str__(self):
        return self.name



