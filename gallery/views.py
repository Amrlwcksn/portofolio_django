from django.shortcuts import render
from .models import Gallery

def index(request):
    images = Gallery.objects.all()
    return render(request, 'gallery/index.html', {'images': images})
