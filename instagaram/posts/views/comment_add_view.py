from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from posts.models import Post, Comment
from posts.forms import AddCommentForm


class CommentAddView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs.get('pk'))
        form = AddCommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            user = request.user
            Comment.objects.create(author=user, post=post, text=text)
            user.commented_posts.add(post)
        return redirect('main')

    def get_success_url(self):
        print(self.object)
        return redirect('main')
