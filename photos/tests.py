from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.
class ImageTestCase(TestCase):

    #set up method
    def setUp(self):
        self.location=Location(location='Nai')
        self.location.save()
        self.sharry=Image(image='1', name='cat', location=self.location, description='cat purring')

        # self.category = Category(category='test')
        # self.category.save_category()

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.sharry, Image))

    #Testing save method
    def test_save_method(self):
        self.sharry.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images) > 0)
    
    #creating a new tag and saving it

        self.new_image=Image(image='', name='lady in Bali', description='lady in bali', location=self.location)
        self.new_image.save()

    #deleting an image
    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    #updating image
    def test_update_image(self):
        self.sharry.save_image()
        self.sharry.update_image('test')
        self.assertTrue(self.sharry.image=='test')
    
    #searching image by id 

    def search_by_id(self):
        self.sharry.save_image()
        found_image = self.sharry.search_by_id(self.sharry.id)
        image = Image.objects.filter(id=self.sharry.id)
        self.assertTrue(found_image, image)

    # def test_search_image_by_location(self):
    #     self.sharry.save_image()
    #     found_images = self.sharry.filter_by_location(location='Kinoo')
    #     self.assertTrue(len(found_images) == 1)

    # def test_search_image_by_category(self):
    #     self.sharry.save_image()
    #     found_img = self.sharry.search_by_category(category=self.category)
    #     self.assertTrue(len(found_img) == 1)
    
# class TestLocation(TestCase):
#     def setUp(self):
#         self.location = Location(name='Kinoo')
#         self.location.save_location()

#     def test_instance(self):
#         self.assertTrue(isinstance(self.location, Location))

#     def test_save_location(self):
#         self.location.save()
#         locations = Location.get_locations()
#         self.assertTrue(len(locations) > 0)

#     def test_get_locations(self):
#         # self.location.save_location()
#         loc = Location(name="Uganda")
#         loc.save_location()
#         locations = Location.objects.all()
#         self.assertTrue(len(locations) > 1)

#     def test_update_location(self):
#         new_location = 'Eldoret'
#         self.location.update_location(self.location.id, new_location)
#         changed_location = Location.objects.filter(name='Eldoret')
#         self.assertTrue(len(changed_location) > 0)

#     def test_delete_location(self):
#         self.location.delete_location()
#         location = Location.objects.all()
#         self.assertTrue(len(location) == 0)
