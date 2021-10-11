from django.shortcuts import render
from django.http import HttpResponse

from .models import Category, Image

# Create your views here.
def gallery(request):
    categories= Category.objects.all()
    photos=Image.objects.all()

    context= { 'categories': categories, 'photos':photos }
    return render(request,'all-pics/gallery.html', context)

def newPhoto(request):
    categories=Category.objects.all()
    
    context= { 'categories': categories,}
    return render (request, 'all-pics/new.html', context)

def photo(request):
    photo=Image.objects.get()
    return render(request, 'all-pics/photo.html', {'photo':photo})