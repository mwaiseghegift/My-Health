from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog, About, Gallery
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError
from .forms import AmountForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

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
        'footer_gallery': Gallery.objects.all().order_by('-date_upload')[:6]
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
        'footer_gallery': Gallery.objects.all().order_by('-date_upload')[:6],
    }

def BlogDetailView(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    
    context = {
        'post':post,
        'footer_gallery': Gallery.objects.all().order_by('-date_upload')[:6],
    }
    return render(request, 'blog_detail.html', context)

def SupportView(request, *args, **kwargs):
    
    amount = ""    
    
    if request.method == 'POST':
        form = AmountForm(request.POST)
        
        if form.is_valid():
            amount = form.cleaned_data['amount']
            request.session['amount'] = amount
            redirect('mainapp:paypall')
                 
        else:
            form = AmountForm()
        
    
    context = {
        'amount':amount,
        'footer_gallery': Gallery.objects.all().order_by('-date_upload')[:6],
    }
    
    return render(request, 'support.html', context)

def PaypallCheckout(request, *args, **kwargs):
    amount = request.session.get('amount')
    print(amount)
    
    context = {
        'footer_gallery': Gallery.objects.all().order_by('-date_upload')[:6],
    }

    
    return render(request, 'paypall.html', context)

def AboutView(request, *args, **kwargs):
    context = {
        'about': About.objects.all(),
        'footer_gallery': Gallery.objects.all().order_by('-date_upload')[:6],
    }
    return render(request, 'about.html', context)

def ContactView(request, *args, **kwargs):
    context = {
        'footer_gallery': Gallery.objects.all().order_by('-date_upload')[:6],
    }
    return render(request, 'contact.html', context)


