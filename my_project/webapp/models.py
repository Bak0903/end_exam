from django.db import models
from django.urls import reverse
from django.conf import settings


class SoftDeleteManager(models.Manager):
    def active(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Автор')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    death_date = models.DateField(null=True, blank=True, verbose_name='Дата смерти')
    biography = models.TextField(null=True, blank=True, max_length=2000, verbose_name='Биография')
    is_deleted = models.BooleanField(default=False)
    objects = SoftDeleteManager()

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return reverse('webapp:author', kwargs={'pk': self.pk})


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Автор')
    published_year = models.CharField(max_length=4, null=True, blank=True, verbose_name='Год издания')
    file = models.FileField(null=True, blank=True, verbose_name='Файл')
    picture = models.ImageField(null=True, blank=True, verbose_name='Обложка')
    description = models.TextField(null=True, blank=True, max_length=2000, verbose_name='Описание')

    def __str__(self):
        return "%s (%s)" % (self.name, self.published_year)

    def get_absolute_url(self):
        return reverse('webapp:book', kwargs={'pk': self.pk})
