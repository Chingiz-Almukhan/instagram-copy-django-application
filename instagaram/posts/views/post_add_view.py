from django.views.generic import CreateView

from posts.models import Post
from posts.forms import AddPostForm


class PostAddView(CreateView):
    template_name = 'add_post.html'
    success_url = ('/')
    model = Post
    form_class = AddPostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
