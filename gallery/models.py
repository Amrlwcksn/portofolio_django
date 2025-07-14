from django.db import models

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/img/')
    is_featured = models.BooleanField(default=False)

def __str__(self):
    return f"Image {self.id}"

