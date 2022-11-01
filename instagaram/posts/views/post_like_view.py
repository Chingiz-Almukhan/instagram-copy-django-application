from django.shortcuts import redirect, get_object_or_404
from django.views import View
from posts.models import Post


class LikeAddView(View):

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        if request.user in post.user_likes.all():
            post.user_likes.remove(request.user)
            return redirect('main')
        post.user_likes.add(request.user)
        return redirect('main')
