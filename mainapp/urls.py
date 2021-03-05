from django.urls import path
from .views import (IndexView,
                    BlogView,
                    BlogDetailView,
                    SupportView,
                    AboutView,
                    ContactView, 
                    PaypallCheckout,
                    ModView,     
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
  path('index2/', ModView, name="index2"), 
]
