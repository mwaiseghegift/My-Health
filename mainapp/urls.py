from django.urls import path
from .views import (IndexView,
                    BlogView,
                    BlogDetailView,
                    SupportView,
                    AboutView,
                    ContactView, 
                    PaypallCheckout,
                    getAccessToken,
                    LipaNaMpesaOnline,    
                    )


app_name = 'mainapp'

urlpatterns = [
  path('', IndexView, name="index"),
  path('blog/', BlogView, name="blog-list"),
  path('blog/<slug>/', BlogDetailView, name='blog-detail'),
  path('support/', SupportView, name="support"),
  path('support/checkout/',PaypallCheckout, name='paypall'),
  path('contact/', ContactView, name='contact'),
  path('about/', AboutView, name="about"),
  path('access/token/', getAccessToken, name="get_mpesa_access_token"),
  path('online/lipa/', LipaNaMpesaOnline, name='lipa_na_mpesa'), 
]
