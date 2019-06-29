from django.urls import path
from webapp.views.author import AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, delete_author
from webapp.views.book import BookListView, BookDetailView, BookCreateView, BookUpdateView, delete_book, download_file
from webapp.views.user import UserView, UserListView, add_to_bookcase, remove_from_bookcase
from webapp.views.comment import comment

app_name = 'webapp'

urlpatterns = [
    path('user/<int:pk>/', UserView.as_view(), name = 'user_detail'),
    path('users/', UserListView.as_view(), name='users'),

    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author'),
    path('author/create/', AuthorCreateView.as_view(), name='create_author'),
    path('author/<int:pk>/update/', AuthorUpdateView.as_view(), name='update_author'),
    path('author/<int:author_pk>/delete/', delete_author, name='delete_author'),

    path('', BookListView.as_view(), name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book'),
    path('book/create/', BookCreateView.as_view(), name='create_book'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='update_book'),
    path('book/<int:book_pk>/delete/', delete_book, name='delete_book'),
    path('download/<int:book_pk>', download_file, name='download'),


    path('add/to/bookcase/<int:book_pk>', add_to_bookcase, name='add_to_bookcase'),
    path('remove/from/bookcase/<int:book_pk>', remove_from_bookcase, name='remove_from_bookcase'),

    path('book/comment/create/', comment, name='create_comment'),
]
