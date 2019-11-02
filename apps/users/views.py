from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse_lazy
from django.views import generic

from .forms import LoginForm
from .forms import UserCreationForm


class SignupPageView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("home")
    template_name = "signup.html"


class LoginView(BaseLoginView):
    """ログインページ"""

    form_class = LoginForm
    template_name = "login.html"


class HomeView(generic.TemplateView):
    template_name = "home.html"
