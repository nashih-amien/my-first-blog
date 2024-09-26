from django.contrib import admin

# Register your models here.
from .models import Post, comment

admin.site.register(Post)
admin.site.register(comment)