from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from webapp.models import Author
from webapp.forms import AuthorForm


class BaseView(LoginRequiredMixin, TemplateView):
    template_name = 'base.html'


class AuthorListView(ListView):
    model = Author
    template_name = 'Author/list.html'

    def get_queryset(self):
        return Author.objects.active()


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'Author/detail.html'

    def get_queryset(self):
        return Author.objects.active()

class AuthorCreateView(CreateView):
    model = Author
    template_name = 'Author/create.html'
    form_class = AuthorForm


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'Author/update.html'
    form_class = AuthorForm

    def get_queryset(self):
        return Author.objects.active()


def delete_author(request, author_pk):
    author = get_object_or_404(Author, pk=author_pk)
    author.is_deleted = True
    author.save()
    return redirect('webapp:authors')
