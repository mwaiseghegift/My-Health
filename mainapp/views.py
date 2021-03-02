from django.shortcuts import render

# Create your views here.

def IndexView(request, *args, **kwargs):
    context = {
        
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
