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

        # Jika panjang title lebih dari 30, maka panjang content tidak boleh lebih dari 50
        if title is not None and content is not None:
            if len(title) > 30 and len(content) > 50:
                self.add_error('content', "Jika title lebih dari 30 karakter, content tidak boleh lebih dari 50 karakter.")

class PostEdit(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('text', 'tag')

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['content']