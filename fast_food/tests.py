import django
from django.test import TestCase
from .models import About, BookTable, Type
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings


class ModelTestCase(TestCase):

    def setUp(self):
        pass


    def test_region_object_count(self):
        fo = Type(name="Burger")
        fo.save()
        

        self.assertEquals(Type.objects.all().count(), 1 ,msg="the type count error")

    def test_region_object_create(self):
        fo = Type(name="Burger")
        fo.save()
        

        self.assertEquals(fo,Type.objects.get(name='Burger' ),msg="the type create error")
        
        
class ViewTest(TestCase):
     
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.force_login(self.user)
        return super().setUp()

    def test_create_food_view_post(self):

        tp = Type(name='Burger')
        tp.save()
        
        
    
        response = self.client.post(reverse('create'), { 
            "name": 'test name',
            "type": tp.id,
            "price": 0,
            "description": 'test description',
            "image": SimpleUploadedFile(name='test', content=open(settings.BASE_DIR / 'media' / 'book-images' / 'images.jpg', 'rb').read(), content_type='images/jpeg'),
        })
        assert response.status_code == 200


# class ModelTestCase(TestCase):

#     def setUp(self):
#         pass


#     def test_region_object_count(self):
#         fo = About(name="")
#         fo.save()
        

#         self.assertEquals(About.objects.all().count(), 1 ,msg="the type count error")

#     def test_region_object_create(self):
#         fo = About(name="")
#         fo.save()
        

#         self.assertEquals(fo,About.objects.get(name='Burger' ),msg="the type create error")
        
        
# class ViewTest(TestCase):
     
#     def setUp(self):
#         self.user = User.objects.create(username='testuser')
#         self.user.set_password('12345')
#         self.user.save()
#         self.client.force_login(self.user)
#         return super().setUp()

#     def test_create_food_view_post(self):

#         tp = Type(name='Burger')
#         tp.save()
    
#         response = self.client.post(reverse('create')), { 
#             "name": 'test name',
#             "type": tp.id,
#             "price": 0,
#             "description": 'test description',
#             "image": SimpleUploadedFile(name='test',content=open(settings.BASE_DIR / 'media' / 'book-images' /'pexels-rajesh-tp-1633578_VJKrnYn.jpg','r').read(),content_type='images/jpeg'),
#         }
#         assert response.status_code == 200

# class ModelTestCase(TestCase):

#     def setUp(self):
#         pass


#     def test_region_object_count(self):
#         fo = BookTable(name="")
#         fo.save()
        

#         self.assertEquals(BookTable.objects.all().count(), 1 ,msg="the type count error")

#     def test_region_object_create(self):
#         fo = BookTable(name="")
#         fo.save()
        

#         self.assertEquals(fo,BookTable.objects.get(name='Burger' ),msg="the type create error")