from django.contrib import admin
from webapp.models import Author, Book, Bookcase, Comment

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Bookcase)
admin.site.register(Comment)
