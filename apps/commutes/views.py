from django.views import generic

from .models import Commute


class CommuteListView(generic.ListView):
    model = Commute
    context_object_name = "commutes"
    template_name = "commutes/list.html"
