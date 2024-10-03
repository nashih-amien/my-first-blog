from django import forms

from .models import Post, comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'tag')

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if any(char.isdigit() for char in title):
            raise forms.ValidationError("Title tidak boleh mengandung angka.")
        return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

class PostEdit(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('text', 'tag')

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['content']