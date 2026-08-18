from django.shortcuts import get_object_or_404, redirect, render

from apps.events.models import Registration


def my_tickets(request):
    registrations = Registration.objects.none()
    email = request.GET.get("email", "").strip()
    if email:
        registrations = Registration.objects.filter(email__iexact=email).select_related("event")
    return render(request, "tickets/index.html", {"registrations": registrations, "email": email})


def ticket_detail(request, reference):
    registration = get_object_or_404(
        Registration.objects.select_related("event"), reference=reference
    )
    return render(request, "tickets/detail.html", {"registration": registration})


def verify(request):
    reference = request.GET.get("reference", "").strip()
    if reference:
        return redirect("tickets:detail", reference=reference)
    return render(request, "tickets/verify.html")
