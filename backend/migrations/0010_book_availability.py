# Generated by Django 3.1.6 on 2021-02-24 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='availability',
            field=models.IntegerField(default=0),
        ),
    ]
