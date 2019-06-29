from django.shortcuts import redirect
from webapp.models import Comment


def comment(request):
    book_id = request.POST.get('book_id', '/')
    text = request.POST.get('text', '/')
    user_id = request.user.pk
    if request.user:
        Comment.objects.create(book_id=book_id, user_id=user_id, text=text)
    return redirect('webapp:book', pk=book_id)
