from django.conf.urls import url 
from . import views
import photos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
     url('^$',views.gallery,name='gallery-photos'),
     # url('^$photo/',views.photo,name='view-pictures'),
     # url('^$new/',views.newPhoto,name='new-photos'),
    url('^photo/$',views.photo,name = 'view-pictures'),
    url('^new/$',views.newPhoto,name = 'new-pictures'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)