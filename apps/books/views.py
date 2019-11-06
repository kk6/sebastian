from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView

from .forms import BookPurchaseForm
from .models import BookPurchase


class BookPurchaseListView(LoginRequiredMixin, ListView):
    """書籍の購入履歴の一覧ページ"""

    model = BookPurchase
    context_object_name = "book_purchases"
    template_name = "books/list.html"


class BookPurchaseCreateView(LoginRequiredMixin, CreateView):
    """書籍の購入履歴の登録ページ"""

    model = BookPurchase
    form_class = BookPurchaseForm
    template_name = "books/purchase.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        f = form.save(commit=False)
        f.user = self.request.user
        f.save()
        return super().form_valid(form)
