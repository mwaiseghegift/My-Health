from django.db import models
from PIL import Image
from django.urls import reverse
from django.contrib.auth import get_user_model

from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

from tinymce.models import HTMLField

from django.utils import timezone 
from django.utils.text import slugify


# Create your models here.

User=get_user_model()



class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_user")
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/blog/%Y/%m/%d")
    image_thumbnail = ImageSpecField(source = 'image',
                                     processors = [ResizeToFill(620,154)],
                                     format = 'JPEG',
                                     options = {'quality':100})
    content = HTMLField()
    pub_date = models.DateTimeField(default=timezone.now)
    slug=models.SlugField(unique=True, blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.user}"
    
    def get_absolute_url(self):
        return reverse("mainapp:blog_detail", kwargs={"slug": self.slug})
    
    @property
    def no_of_comments(self):
        return Comment.objects.filter(post=self).count()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    class Meta:
        ordering = ["-pub_date"]
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_comment")
    content = HTMLField()
    parent = models.ForeignKey("self", on_delete=models.CASCADE, 
                               null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.author.username +' - '+self.content
    
    def replies(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent != None:
            return False
        return True
    
class About(models.Model):
    about = HTMLField()
    mission = HTMLField()
    
    def __str__(self):
        return f"{self.about}"
    
class ImageProcessor(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/slides/')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(960, 360)],
                                     format='JPEG',
                                     options = {'quality':150},
                                     )
    date_upload = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.image_thumbnail.url}"
    
class Gallery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/gallery")
    image_thumbnail = ImageSpecField(source='image',
                                     processors = [ResizeToFill(75,75)],
                                     format='JPEG',
                                     options = {'quality':60},
                                     )
    date_upload = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    