from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.
class ImageTestCase(TestCase):

    #set up method
    def setUp(self):
        self.sharry=Image(image_id='1', name='cat', description='cat purring')
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.sharry, Image))
