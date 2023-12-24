from django.forms import ModelForm

from showroom.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['car']
