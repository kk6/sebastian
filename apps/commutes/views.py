from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .appmodels import CommuteApp
from .forms import CommuteForm
from .forms import CommuteUpdateForm
from .models import Commute
from .repositories import CommuteRepository


class CommuteListView(generic.ListView):
    model = Commute
    context_object_name = "commutes"
    template_name = "commutes/list.html"
    ordering = ["-date_of_use", "usage_type"]
    repository = CommuteRepository()

    def get_queryset(self):
        object_list = self.repository.get_user_commutes(
            self.request.user.pk, self.ordering
        )
        return object_list


class CommuteUpdateView(generic.UpdateView):
    model = Commute
    form_class = CommuteUpdateForm
    success_url = reverse_lazy("commute_list")
    template_name = "commutes/edit.html"


class CommuteDeleteView(generic.DeleteView):
    model = Commute
    success_url = reverse_lazy("commute_list")
    template_name = "commutes/delete.html"


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