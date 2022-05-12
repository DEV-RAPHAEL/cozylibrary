from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.BookListView.as_view(), name="home"),
    path("book/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("book/new/", views.BookCreateView.as_view(), name="book_new"),
    path("book/<int:pk>/update/", views.BookUpdateView.as_view(), name="book_update"),
    path("book/<int:pk>/delete/", views.BookDeleteView.as_view(), name="book_delete"),
    path("search", views.search, name="book_search"),
    path("category/<str:category>/", views.category, name="book_category"),
    path("popular/", views.popular, name="book_popular"),
    path("recent", views.recently_added, name="book_recent"),
    path("about", views.about, name="book_about"),
    path("profile", views.profile, name="profile"),
]

admin.site.site_header = "Cozy Library Dashboard"
admin.site.site_title = "Cozy Library"
admin.site.index_title = "Welcome to the Cozy Library"
