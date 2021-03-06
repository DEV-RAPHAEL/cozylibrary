from django.db import models
from django.utils.timezone import datetime
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here


class Book(models.Model):
    title = models.CharField(max_length=255, default="Dapo Adedire")
    author = models.CharField(max_length=255, default="Dapo Adedire")
    category = models.CharField(max_length=255, blank=True)
    pages = models.IntegerField(default=0)
    price = models.FloatField(default=0.99)
    year = models.IntegerField(default=0)
    language = models.CharField(max_length=255, default="English")
    description = RichTextField(max_length=1000, blank=True)
    cover_image = models.ImageField(upload_to="covers/", default="/covers/default.jpg")
    created_at = models.DateTimeField(default=datetime.now)
    views = models.IntegerField(default=0)
    book = models.FileField(default="/books/default.pdf", upload_to="books/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])

    def views_increment(self):
        self.views += 1
        self.save()
