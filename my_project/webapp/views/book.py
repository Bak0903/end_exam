import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from webapp.models import Author, Book
from webapp.forms import BookForm


class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'

    def get_queryset(self):
        return Book.objects.active()


class BookDetailView(DetailView):
    model = Author
    template_name = 'book/book_detail.html'

    def get_queryset(self):
        return Book.objects.active()


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    template_name = 'book/book_create.html'
    form_class = BookForm

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user.is_staff


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    template_name = 'book/book_update.html'
    form_class = BookForm

    def get_queryset(self):
        return Book.objects.active()

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user.is_staff


def delete_book(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    if request.user.is_staff:
        book.is_deleted = True
        book.save()
    return redirect('webapp:author', pk=book.author.pk)


def download_file(request, book_pk):
    book = get_object_or_404(Book, pk = book_pk)
    path = book.file.path
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/file")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
