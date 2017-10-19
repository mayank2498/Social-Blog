from django.contrib import admin
from .models import Blog


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ["author", "description", "title", "image","pk"]

admin.site.register(Blog,BlogAdmin)

