from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView, ProfileView, UserChangeView, SubscribeAddView, \
    SubscribersView, FollowView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('subscribe/<int:pk>', SubscribeAddView.as_view(), name='subscribe'),
    path('profile/<int:pk>/change/', UserChangeView.as_view(), name='edit_profile'),
    path('profile/<int:pk>/subscribers', SubscribersView.as_view(), name='subscribers'),
    path('profile/<int:pk>/follows', FollowView.as_view(), name='follows'),
    path('logout/', logout_view, name='logout')
]
