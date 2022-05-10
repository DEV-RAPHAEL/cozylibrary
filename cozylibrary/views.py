from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from . import models


class BookListView(ListView):
    model = models.Book
    context_object_name = 'books'
    template_name = 'home.html'

    def get_queryset(self):
        return models.Book.objects.all().order_by('-created_at')


class BookDetailView(DetailView):
    model = models.Book
    context_object_name = 'book'
    template_name = 'book_detail.html'