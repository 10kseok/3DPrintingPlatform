from django.shortcuts import render
from django.views import generic

from trade.models import Estimate
# Create your views here.

class EstimatesView(generic.ListView):
    template_name: str = "../templates/buyer_main.html"
    context_object_name = "estimates"

    def get_queryset(self):
        return Estimate.objects.all()
