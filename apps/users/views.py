from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse_lazy
from django.views import generic

from .forms import LoginForm
from .forms import UserCreationForm


class SignupView(generic.CreateView):
    """ユーザー登録ページ"""

    form_class = UserCreationForm
    success_url = reverse_lazy("dashboard")
    template_name = "users/signup.html"


class LoginView(BaseLoginView):
    """ログインページ"""

    form_class = LoginForm
    template_name = "users/login.html"
