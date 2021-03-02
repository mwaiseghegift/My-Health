from django.contrib import admin
from .models import (
    Blog,
    Comment,
    About,
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
admin.site.register(About)