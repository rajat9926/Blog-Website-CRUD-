from django.contrib import admin
from .models import BlogPost_table

@admin.register(BlogPost_table)
class BlogPostTableAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','user']