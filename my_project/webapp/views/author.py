from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from webapp.models import Author, Book
from webapp.forms import AuthorForm


class AuthorListView(ListView):
    model = Author
    template_name = 'author/author_list.html'

    def get_queryset(self):
        return Author.objects.active()


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author/author_detail.html'

    def get_queryset(self):
        return Author.objects.active()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(author=self.object.pk, is_deleted=False)
        return context


class AuthorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Author
    template_name = 'author/author_create.html'
    form_class = AuthorForm

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user.is_staff


class AuthorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Author
    template_name = 'author/author_update.html'
    form_class = AuthorForm

    def get_queryset(self):
        return Author.objects.active()

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user.is_staff


def delete_author(request, author_pk):
    if request.user.is_staff:
        author = get_object_or_404(Author, pk=author_pk)
        author.is_deleted = True
        author.save()
    return redirect('webapp:authors')
