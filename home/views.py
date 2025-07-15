from django.shortcuts import render
from gallery.models import Gallery  
from blog.models import Post  # ← typo sebelumnya: `model` harusnya `models`

def index(request):
    # Ambil 2 gambar highlight dari galeri
    featured_images = Gallery.objects.filter(is_featured=True)[:2]

    # Ambil 2 postingan blog terbaru
    highlight_posts = Post.objects.order_by('-created_at')[:2]

    return render(request, 'home/index.html', {
        'featured_images': featured_images,
        'highlight_posts': highlight_posts,
    })
