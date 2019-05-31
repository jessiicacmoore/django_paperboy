from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import DeliveryForm

from .models import Paperboy


def root(request):
    form = DeliveryForm()

    context = {
        "paperboys": Paperboy.objects.all(),
        "total_delivered": Paperboy.total_delivered(),
        "total_earned": Paperboy.total_earned,
        "form": form,
    }
    response = render(request, "index.html", context)
    return HttpResponse(response)


def make_delivery(request, id):
    selected_paperboy = Paperboy.objects.get(id=id)
    if request.method == "POST":
        form = DeliveryForm(request.POST)
        if form.is_valid():
            start_address = form.cleaned_data.get("starting_house_number")
            end_address = form.cleaned_data.get("ending_house_number")
            selected_paperboy.deliver(
                start_address=start_address, end_address=end_address
            )
            selected_paperboy.save()
            return redirect("home")
        else:
            root()
