# Generated by Django 3.1.6 on 2021-02-15 14:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0004_auto_20210215_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='user_rating',
            field=models.ManyToManyField(blank=True, null=True, related_name='book_rating', to=settings.AUTH_USER_MODEL),
        ),
    ]
