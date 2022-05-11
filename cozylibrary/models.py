from django.db import models
from django.utils.timezone import datetime
from django.urls import reverse
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True)
    pages = models.IntegerField(default=0)
    price = models.FloatField(default=0.99)
    year = models.IntegerField(default=0)
    language = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    cover_image = models.ImageField(upload_to='covers/', default='/covers/default.jpg')
    created_at = models.DateTimeField(default=datetime.now)
    views = models.IntegerField(default=0)  


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

    def views_increment(self):
        self.views += 1
        self.save()