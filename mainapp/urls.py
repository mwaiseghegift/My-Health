from django.urls import path
from .views import (IndexView,
                    BlogView,
                    BlogDetailView,
                    SupportView,
                    AboutView,
                    ContactView,      
                    )


app_name = 'mainapp'

urlpatterns = [
  path('', IndexView, name="index"),
  path('blog/', BlogView, name="blog-list"),
  path('support/', SupportView, name="support"),
  path('contact/', ContactView, name='contact'),
  path('about/', AboutView, name="about"), 
]
