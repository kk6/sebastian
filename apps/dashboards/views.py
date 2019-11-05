import datetime

from books.models import BookPurchase
from django.shortcuts import redirect
from django.views import generic


class IndexView(generic.TemplateView):
    """Indexページ"""

    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard")
        return super().dispatch(request, *args, **kwargs)


class DashboardView(generic.ListView):
    """ホーム"""

    model = BookPurchase
    context_object_name = "book_purchases"
    template_name = "dashboards/dashboard.html"

    def get_queryset(self):
        return self.model.objects.filter(
            user=self.request.user,
            purchase_at__gte=(datetime.date.today() - datetime.timedelta(days=31)),
        )
