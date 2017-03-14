from django.contrib import admin
from .models import Post  # . denotes that the models file is in the same directory as admin.py

# Register your models here.
admin.site.register(Post)