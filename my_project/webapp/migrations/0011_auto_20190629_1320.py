# Generated by Django 2.2.2 on 2019-06-29 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20190629_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Author', verbose_name='Автор'),
        ),
    ]
