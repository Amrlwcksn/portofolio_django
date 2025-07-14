from django.shortcuts import render
from gallery.models import Gallery  # ← Pastikan ini ada

def index(request):
    featured_images = Gallery.objects.filter(is_featured=True)[:2]  # Ambil 2 gambar
    return render(request, 'home/index.html', {
        'featured_images': featured_images,
    })
