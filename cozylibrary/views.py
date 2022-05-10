from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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


class BookCreateView(CreateView):
    model = models.Book
    fields = '__all__'
    template_name = 'book_new.html'


class BookUpdateView(UpdateView):
    model = models.Book
    fields = '__all__'
    template_name = 'book_update.html'


class BookDeleteView(DeleteView):
    model = models.Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('home')
