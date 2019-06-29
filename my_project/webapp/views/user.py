from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView


class UserView(DetailView):
    model = User
    template_name = 'user/user_detail.html'


class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'

    # def get_queryset(self):
    #     return User.objects.exclude(is_superuser=True)
