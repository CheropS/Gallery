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
    @classmethod
    def get_locations(cls):
        return Location.objects.all()

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(name=value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


    
          

class Image(models.Model):
    image_id=models.CharField(max_length=100)
    image=models.ImageField(null=False, blank=False)
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=500)
    location=models.ForeignKey(Location, on_delete=models.CASCADE)
    category=models.ManyToManyField(Category)

    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
    def update_image(self,value):
        self.image=value
        self.save_image()

    @classmethod
    def search_by_id(cls, search_term):
        photos=cls.objects.filter(id__icontains=search_term)
        return photos
   
    @classmethod
    def filter_by_location(cls, location):
        return Image.objects.filter(location__name=location).all()
        
    @classmethod
    def search_by_category(cls, category):
        return cls.objects.filter(category__name__icontains=category)
