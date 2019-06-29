from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Автор')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    death_date = models.DateField(null=True, blank=True, verbose_name='Дата смерти')
    biography = models.TextField(null=True, blank=True, max_length=2000, verbose_name='Биография')
