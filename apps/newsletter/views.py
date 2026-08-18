from django.contrib import messages
from django.shortcuts import redirect

from .services import subscribe


def subscribe_view(request):
    if request.method == "POST" and request.POST.get("email"):
        subscribe(request.POST["email"].strip())
        messages.success(request, "You are subscribed to parish updates.")
    return redirect(request.META.get("HTTP_REFERER", "/"))
