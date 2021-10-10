from django.conf.urls import url 
from . import views
import photos

urlpatterns=[
     url('^$',views.gallery,name='gallery-photos'),
     # url('^$photo/',views.photo,name='view-pictures'),
     # url('^$new/',views.newPhoto,name='new-photos'),
    url('^photo/$',views.photo,name = 'view-pictures'),
    url('^new/$',views.newPhoto,name = 'new-pictures'),
]