from django.db import models
from ckeditor.fields import RichTextField
from backend.models import Book
from django.contrib.auth.models import User


class Comment(models.Model):
    book = models.ForeignKey(Book, related_name='comment', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(null=True, blank=True, config_name='comment')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.book.title, self.name)
