from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog, About, Gallery
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError
from .forms import AmountForm, ContactForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

import requests
from requests.auth import HTTPBasicAuth
import json
from .mpesa_credentials import MpesaAccessToken, LipaNaMpesaPassword
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail


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
    
    return render(request, 'blog.html', context)

def BlogDetailView(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    
    context = {
        'post':post,
        'footer_gallery': Gallery.objects.all().order_by('-date_upload')[:6],
    }
    return render(request, 'blog_detail.html', context)

def SupportView(request, *args, **kwargs):
    
    amount = ""
    telephone = ""    
    
    if request.method == 'POST':
        form = AmountForm(request.POST)
        print("Yes")
        if form.is_valid():
            amount = form.cleaned_data['amount']
            telephone = form.cleaned_data['telephone']
            print(amount)
            print(telephone)
            request.session['amount'] = amount
            
            access_token = MpesaAccessToken.validated_mpesa_access_token
            api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = {"Authorization":"Bearer %s" % access_token}
            request = {
                "BusinessShortCode": LipaNaMpesaPassword.business_short_code,
                "Password": LipaNaMpesaPassword.decode_password,
                "Timestamp": LipaNaMpesaPassword.lipa_time,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": f"{amount}",
                "PartyA": f"{telephone}",
                "PartyB": "174379",
                "PhoneNumber": f"{telephone}",
                "CallBackURL": "https://myhealthke.pythonanywhere.com/saf",
                "AccountReference": "MyHealth",
                "TransactionDesc": "myhealth test"
            }
            response = requests.post(api_url, json=request, headers=headers)
            return HttpResponseRedirect('/support/checkout/')
                 
        else:
            form = AmountForm()
            

    
    context = {
        'amount':amount,
        'telephone':telephone,
        'footer_gallery': Gallery.objects.all().order_by('-date_upload')[:6],
    }
    
    return render(request, 'support.html', context)

def PaypallCheckout(request, *args, **kwargs):
    amount = request.session.get('amount')
    print(amount)
    context = {
        'amount':amount,
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, email, ['itsregalo047@gmail.com'], fail_silently=False)
        
        else:
            form = ContactForm()
    
    context = {
        'footer_gallery': Gallery.objects.all().order_by('-date_upload')[:6],
    }
    return render(request, 'contact.html', context)

def getAccessToken(request):
    consumer_key = 'n9KbDodntGKwIpwrENmqwghaXk18WstU'
    consumer_secret = 'TGxmOUSsa4FK4cuD'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    
    return HttpResponse(validated_mpesa_access_token)


def LipaNaMpesaOnline(request):
    pass
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization":"Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipaNaMpesaPassword.business_short_code,
        "Password": LipaNaMpesaPassword.decode_password,
        "Timestamp": LipaNaMpesaPassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "5",
        "PartyA": "254712860997",
        "PartyB": "174379",
        "PhoneNumber": "254712860997",
        "CallBackURL": "https://myhealthke.pythonanywhere.com/saf",
        "AccountReference": "Gift",
        "TransactionDesc": "myhealth test"
    }
    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse('success')



