from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.
from . import models


class BookListView(ListView):
    model = models.Book
    context_object_name = "books"
    template_name = "home.html"

    def get_queryset(self):
        return models.Book.objects.all().order_by("-views")[:25]


class BookDetailView(DetailView):
    model = models.Book

    def get_object(self, queryset=None):
        item = super().get_object(queryset)
        item.views_increment()
        return item

    context_object_name = "book"
    template_name = "book_detail.html"


class BookCreateView(CreateView):
    model = models.Book
    fields = "__all__"
    template_name = "book_new.html"


class BookUpdateView(UpdateView):
    model = models.Book
    fields = "__all__"
    template_name = "book_update.html"


class BookDeleteView(DeleteView):
    model = models.Book
    template_name = "book_delete.html"
    success_url = reverse_lazy("home")


def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        books = models.Book.objects.all().filter(
            Q(title__icontains=searched)
            | Q(author__icontains=searched)
            | Q(category__icontains=searched)
            | Q(description__icontains=searched)
        )
        if books:
            return render(
                request, "book_search.html", {"searched": searched, "books": books}
            )
        else:
            return render(
                request, "book_search.html", {"searched": searched, "books": None}
            )
    else:
        return render(request, "book_search.html", {})


def category(request, category):
    books = models.Book.objects.all().filter(category__icontains=category)
    return render(
        request, "book_category.html", {"books": books, "category": category}
    )

def recently_added(request):
    books = models.Book.objects.all().order_by("-created_at")
    return render(request, "book_recently_added.html", {"books": books})

def about(request):
    return render(request, "about.html")


def profile(request):
    return render(request, "profile.html")