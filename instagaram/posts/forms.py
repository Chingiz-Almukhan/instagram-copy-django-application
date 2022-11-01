from django import forms

from posts.models import Post, Comment


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'image']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Поиск',
                             widget=forms.TextInput(
                                 attrs={'placeholder': "Поиск", 'class': "form-control"}))


class AddCommentForm(forms.ModelForm):
    text = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': "Добавить комментарии", 'class': "form-control border-0 shadow-none"}))

    class Meta:
        model = Comment
        fields = ['text']
