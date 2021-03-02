from django.shortcuts import render
from .models import Blog
from django.utils import timezone

# Create your views here.

def IndexView(request, *args, **kwargs):
    context = {
        'recent_posts':Blog.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
        
    }
    return render(request, 'index.html', context)

def BlogView(request, *args, **kwargs):
    context = {}
    return render(request, 'blog.html', context)

def BlogDetailView(request, *args, **kwargs):
    context = {
        
    }
    return render(request, 'blog_detail.html', context)

def SupportView(request, *args, **kwargs):
    context = {
        
    }
    return render(request, 'support.html', context)

def AboutView(request, *args, **kwargs):
    context = {
        
    }
    return render(request, 'about.html', context)

def ContactView(request, *args, **kwargs):
    context = {
        
    }
    return render(request, 'contact.html', context)
