from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

from accounts.forms import LoginForm, CustomUserCreationForm, UserChangeForm
from accounts.models import Account
from posts.forms import SearchForm
from posts.models import Post


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        next = request.GET.get('next')
        form_data = {} if not next else {'next': next}
        form = self.form(form_data)
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')
        password = form.cleaned_data.get('password')
        if '@' not in form.cleaned_data.get('email'):
            username = form.cleaned_data.get('email')
            email = Account.objects.filter(username=username).values('email')
            if len(email) == 0:
                return redirect('login')
            email_str = email[0]
            user = authenticate(request, email=email_str.get('email'), password=password)
            try:
                login(request, user)
            except Exception:
                return redirect('login')
            return redirect('main')
        email = form.cleaned_data.get('email')
        next = form.cleaned_data.get('next')
        user = authenticate(request, email=email, password=password)
        if not user:
            return redirect('login')
        login(request, user)
        if next:
            return redirect(next)
        return redirect('main')


def logout_view(request):
    logout(request)
    return redirect('login')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
        context = {}
        context['form'] = form
        return self.render_to_response(context)


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SearchForm
        user = self.get_object()
        context['form'] = form
        context['posts'] = Post.objects.filter(author=user).order_by('-created_at')
        return context


class UserChangeView(UserPassesTestMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    def test_func(self):
        return self.request.user == self.get_object()

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})


class SubscribeAddView(View):

    def get(self, request, *args, **kwargs):
        subscribe = get_object_or_404(Account, pk=kwargs.get('pk'))
        if request.user in subscribe.subscriptions.all():
            subscribe.subscriptions.remove(request.user)
            return redirect('profile', pk=kwargs.get('pk'))
        subscribe.subscriptions.add(request.user)
        return redirect('profile', pk=kwargs.get('pk'))


class SubscribersView(DetailView):
    model = get_user_model()
    template_name = 'subscribers.html'
    context_object_name = 'accounts'


class FollowView(DetailView):
    model = get_user_model()
    template_name = 'follows.html'
    context_object_name = 'accounts'
