from django.db import models
from django.urls import reverse


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
