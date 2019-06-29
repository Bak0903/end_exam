from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from webapp.models import Bookcase
from django.views.generic import DetailView, ListView


class UserView(DetailView):
    model = User
    template_name = 'user/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = []
        bookcase = Bookcase.objects.filter(user_id=self.object.pk)
        for item in bookcase:
            if item.book.is_deleted == False:
                context['books'].append(item.book)
        return context


class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'


@csrf_exempt
def add_to_bookcase(request, book_pk):
    if not request.user:
        raise HttpResponseForbidden
    try:
        Bookcase.objects.get(book_id=book_pk, user_id=request.user.pk)
    except:
        Bookcase.objects.create(book_id=book_pk, user_id=request.user.pk)
        return JsonResponse({'status': 'Успешно добавлено!'})
    else:
        return JsonResponse({'status': 'Уже на полке!'})


@csrf_exempt
def remove_from_bookcase(request, book_pk):
    if not request.user:
        raise HttpResponseForbidden
    try:
        Bookcase.objects.get(book_id=book_pk, user_id=request.user.pk).delete()
    except:
        return JsonResponse({'status': 'Такой книги нет, что то пошло не так!'})
    else:
        return JsonResponse({'status': 'Успешно удалено!'})
