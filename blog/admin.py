from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # ⬅️ tampilkan author
    prepopulated_fields = {'slug': ('title',)}
