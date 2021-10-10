from django.db import models


# Create your models here.


class Location(models.Model):
    image_location=models.CharField(max_length=30)

    def __str__(self):
        return self.image_location

class Category(models.Model):
    image_category=models.CharField(max_length=20)
    

    def __str__(self):
        return self.image_category

class Image(models.Model):
    image_id=models.CharField(max_length=1000)
    image_name=models.CharField(max_length=30)
    image_description=models.CharField(max_length=50)
    image_location=models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category=models.ManyToManyField(Category)

    def __str__(self):
        return self.name

