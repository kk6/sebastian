import datetime

from books.models import BookPurchase
from django.contrib.auth.views import LoginView as BaseLoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import LoginForm
from .forms import UserCreationForm


class SignupView(generic.CreateView):
    """ユーザー登録ページ"""

    form_class = UserCreationForm
    success_url = reverse_lazy("home")
    template_name = "users/signup.html"


class LoginView(BaseLoginView):
    """ログインページ"""

    form_class = LoginForm
    template_name = "users/login.html"


class HomeView(generic.ListView):
    """ホーム"""

    model = BookPurchase
    context_object_name = "book_purchases"
    template_name = "users/home.html"

    def get_queryset(self):
        return self.model.objects.filter(
            user=self.request.user,
            purchase_at__gte=(datetime.date.today() - datetime.timedelta(days=31)),
        )


class IndexView(generic.TemplateView):
    """Indexページ

    FIXME: 仮でここに置いているので後々適切な場所に移動

    """

    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)
