# Generated by Django 3.1.6 on 2021-02-15 08:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0003_book_upload_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='user_rating',
            field=models.ManyToManyField(related_name='book_rating', to=settings.AUTH_USER_MODEL),
        ),
    ]
