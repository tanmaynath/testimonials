from django import forms
from .models import Post


class NewPostForm(forms.ModelForm):
    post = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Post
        fields = ['name', 'post']