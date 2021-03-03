from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError

# Create your views here.

def IndexView(request, *args, **kwargs):
    posts = Blog.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date') 
    
    query = request.GET.get('editbox_search',None)
    
    if query is not None:
        posts = Blog.objects.filter(Q(title__icontains=query)|
                                    Q(description__icontains=query)
                                    )
    
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj':page_obj,
    }
    return render(request, 'index.html', context)

def BlogView(request, *args, **kwargs):
    posts = Blog.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date') 
    
    query = request.GET.get('q', None)
    
    if query is not None:
        posts = Blog.objects.filter(Q(title__icontains=query)|
                                    Q(description__icontains=query)
                                    )
    
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj':page_obj,
    }

def BlogDetailView(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    
    context = {
        'post':post,
    }
    return render(request, 'blog_detail.html', context)

def SupportView(request, *args, **kwargs):
    
    query = request.GET.get('your_amount', None)
    
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

def DonationForm(request):
    pass
