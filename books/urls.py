from django.urls import path
from . import views
urlpatterns = [
path('books/', views.book_list, name='book_list'),
path('create/', views.create_book, name='create_book'),
path('update/<pk>/', views.update_book, name='update_book'),
path('delete/<pk>/', views.delete_book, name='delete_book'),
]