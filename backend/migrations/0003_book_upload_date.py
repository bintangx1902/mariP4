# Generated by Django 3.1.6 on 2021-02-14 13:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210213_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
