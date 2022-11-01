
from django.views.generic import DetailView

from posts.forms import SearchForm, AddCommentForm
from posts.models import Post


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SearchForm
        context['form'] = form
        context['comment_form'] = AddCommentForm
        return context
