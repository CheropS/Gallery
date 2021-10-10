from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.
class ImageTestCase(TestCase):

    #set up method
    def setUp(self):
        self.location=Location(location='Nai')
        self.location.save()
        self.sharry=Image(image_id='1', name='cat', location=self.location, description='cat purring')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.sharry, Image))

    #Testing save method
    def test_save_method(self):
        self.sharry.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images) > 0)
    
    #creating a new tag and saving it

        self.new_image=Location(location='Eldoret')
        self.new_image.save()

    #deleting an image
    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()
