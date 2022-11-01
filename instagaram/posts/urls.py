from django.urls import path
from django.contrib.auth.decorators import login_required

from accounts.views import ProfileView
from posts.views.base import PostView
from posts.views.comment_add_view import CommentAddView
from posts.views.post_add_view import PostAddView
from posts.views.post_detail_view import PostDetailView
from posts.views.post_like_view import LikeAddView
from posts.views.search_view import search

urlpatterns = [
    path('', PostView.as_view(), name='main'),
    path('add/post', PostAddView.as_view(), name='add_post'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('post/like/<int:pk>', LikeAddView.as_view(), name='like'),
    path('post/comment/<int:pk>', CommentAddView.as_view(), name='comment'),
    path('search/', search, name='search')

    # path(
    #     route='posts/new/',
    #     view=views.CreatePostView.as_view(),
    #     name='create_post'
    # ),
    #
    # path(
    #     route='posts/<int:post_id>/',
    #     view=login_required(views.PostDetailView.as_view()),
    #     name='detail'
    # ),
]
