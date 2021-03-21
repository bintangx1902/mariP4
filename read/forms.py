from django import forms
from .models import Comment


class AddCommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )
