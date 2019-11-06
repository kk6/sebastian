import datetime

from books.models import BookPurchase
from commutes.repositories import CommuteRepository
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic


class IndexView(generic.TemplateView):
    """Indexページ"""

    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard")
        return super().dispatch(request, *args, **kwargs)


@login_required
def dashboard(request):
    """ダッシュボード"""
    today = datetime.date.today()
    book_purchases = BookPurchase.objects.filter(
        user=request.user, purchase_at__gte=(today - datetime.timedelta(days=31))
    )
    commute_repo = CommuteRepository()
    context = {
        "book_purchases": book_purchases,
        "commutes": commute_repo.get_user_commutes_monthly(
            request.user.pk, today.year, today.month
        ),
    }
    return render(request, "dashboards/dashboard.html", context)
