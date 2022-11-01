from django.shortcuts import redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from accounts.models import Account
from posts.models import Post, Comment
from posts.forms import AddPostForm, AddCommentForm


class CommentAddView(View):

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs.get('pk'))
        form = AddCommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            user = request.user
            Comment.objects.create(author=user, post=post, text=text)
            user.commented_posts.add(post)
        return redirect('main')

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     form.instance.post = self.request.POST.get('pk')
    #     return super().form_valid(form)

    def get_success_url(self):
        print(self.object)
        return redirect('main')
