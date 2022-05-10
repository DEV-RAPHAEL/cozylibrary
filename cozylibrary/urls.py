from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookListView.as_view(), name='home'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/new/', views.BookCreateView.as_view(), name='book_new'),
    path('book/<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]

admin.site.site_header = 'Cozy Library'
admin.site.site_title = 'Cozy Library'
admin.site.index_title = 'Welcome to the Cozy Library'