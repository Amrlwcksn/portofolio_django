from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field  # ✅ BENAR
from django.utils.html import strip_tags  # Tambahkan ini

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = CKEditor5Field('Konten', config_name='default')
    excerpt = models.TextField(blank=True)  # 🔥 Tambahkan ini
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.excerpt:
            # Potong konten HTML jadi teks biasa, lalu ambil 200 karakter pertama
            self.excerpt = strip_tags(self.content)[:200]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

