from django.contrib import admin
from .models import (
    Blog,
    Comment,
    About,
    ImageProcessor,
    Gallery,
)
admin.site.site_header = "My Health"
admin.site.site_title = "My Health"
# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extras = 2
    
class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ['title','user','pub_date']
    list_filter = ['pub_date']
    search_fields = ['title','user']

admin.site.register(Blog, BlogAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ['about','mission']

admin.site.register(About, AboutAdmin)

class ImageProcessorAdmin(admin.ModelAdmin):
    list_display = ['name','image_thumbnail']
    list_filter = ['date_upload']
    
admin.site.register(ImageProcessor, ImageProcessorAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['date_upload']
    
admin.site.register(Gallery, GalleryAdmin)