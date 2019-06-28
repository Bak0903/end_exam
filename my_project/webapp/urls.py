from django.urls import path
from webapp.views import BaseView

app_name = 'webapp'

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
]
