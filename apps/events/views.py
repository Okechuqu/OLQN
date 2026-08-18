from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EventRegistrationForm
from .models import EventPage, Registration
from .services import registration_total


def register(request, event_slug):
    event = get_object_or_404(EventPage.objects.live().public(), slug=event_slug)
    form = EventRegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        registration = Registration.objects.create(
            event=event,
            name=form.cleaned_data["name"],
            email=form.cleaned_data["email"],
            quantity=form.cleaned_data["quantity"],
            amount=registration_total(event, form.cleaned_data["quantity"]),
        )
        messages.success(request, "Your registration has been created.")
        return redirect("tickets:detail", reference=registration.reference)
    return render(request, "events/register.html", {"event": event, "form": form})


def event_tickets(request, event_slug):
    event = get_object_or_404(EventPage.objects.live().public(), slug=event_slug)
    return render(request, "events/tickets.html", {"event": event})
