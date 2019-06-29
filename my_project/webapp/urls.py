from django.urls import path
from webapp.views import BaseView, AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, delete_author

app_name = 'webapp'

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author'),
    path('author/create/', AuthorCreateView.as_view(), name='create_author'),
    path('author/<int:pk>/update/', AuthorUpdateView.as_view(), name='update_author'),
    path('author/<int:author_pk>/delete/', delete_author, name='delete_author')
]
