from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic

from .appmodels import CommuteApp
from .forms import CommuteForm
from .models import Commute
from .repositories import CommuteRepository


class CommuteListView(generic.ListView):
    model = Commute
    context_object_name = "commutes"
    template_name = "commutes/list.html"


def register_commutes(request):
    """交通費を登録するビュー関数"""
    form = CommuteForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            commute_repo = CommuteRepository()
            commute_app = CommuteApp(commute_repo)
            commute_app.create_commute_by_form(
                user=request.user, **form.get_cleaned_results()
            )
            return redirect("commute_list")
    context = {"form": form}
    return render(request, "commutes/register.html", context)
