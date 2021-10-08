from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def gallery(request):
    return render(request,'all-pics/gallery.html')

def newPhoto(request):
    return render (request, 'photos/new.html')

def photo(request):
    return render(request, 'photos/photo.html')