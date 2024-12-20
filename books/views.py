
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm
from django.core.paginator import Paginator
def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 10) 
    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
        paginator = Paginator(books, 10)  
        page_number = request.GET.get('page')
        books = paginator.get_page(page_number)
    return render(request, 'books/book_list.html', {'books': books})

@login_required
def create_book(request):
 if request.method == 'POST':
  form = BookForm(request.POST)
  if form.is_valid():
   form.save()
  return redirect('book_list')
 else:
  form = BookForm()
 return render(request, 'books/create_book.html', {'form': form})

@login_required
def update_book(request, pk):
 book = Book.objects.get(pk=pk)
 if request.method == 'POST':
  form = BookForm(request.POST, instance=book)
  if form.is_valid():
   form.save()
   return redirect('book_list')
 else:
  form = BookForm(instance=book)
 return render(request, 'books/update_book.html', {'form': form})

@login_required
def delete_book(request, pk):
 book = Book.objects.get(pk=pk)
 if request.method == 'POST':
  book.delete()
  return redirect('book_list')
 return render(request, 'books/delete_book.html', {'book': book})