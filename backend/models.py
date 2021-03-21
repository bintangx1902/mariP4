from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    link = models.SlugField(max_length=255, unique=True, default='')
    book = models.FileField(upload_to='book/pdf/')
    cover = models.ImageField(upload_to='book/cover/')
    author = models.CharField(max_length=255)
    availability = models.IntegerField(default=0)
    description = RichTextField(null=True, blank=True, config_name='special')
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    pending = models.BooleanField(default=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    user_rating = models.ManyToManyField(User, related_name='book_rating', blank=True)
    category = models.ManyToManyField(Category)

    def total_rating(self):
        if self.rating == 0 and self.user_rating.count() == 0:
            return self.rating
        else:
            a = int(self.rating)
            b = self.user_rating.count()
            c = a / int(b)
            return c

    def current_rate(self):
        return int(self.rating)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.book.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return self.link
