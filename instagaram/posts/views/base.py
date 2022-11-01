from urllib.parse import urlencode

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.views.generic import ListView

from accounts.models import Account
from posts.forms import SearchForm, AddCommentForm
from posts.models import Post


class PostView(ListView):
    template_name = 'feed.html'
    model = Post
    context_object_name = 'posts'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = SearchForm()
        context['comment_form'] = AddCommentForm()
        return context
