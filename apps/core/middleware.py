from django.conf import settings
from django.http import Http404
from django.shortcuts import render


class FriendlyErrorPagesMiddleware:
    """Render branded browser errors even when Django's debug pages are enabled."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if self._should_replace(request, response.status_code):
            friendly_response = render(
                request,
                f"{response.status_code}.html",
                status=response.status_code,
            )
            friendly_response["X-Original-Error-Status"] = str(response.status_code)
            return friendly_response
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, Http404):
            return None
        if self._should_replace(request, 500):
            return render(request, "500.html", status=500)
        return None

    @staticmethod
    def _should_replace(request, status_code):
        if not getattr(settings, "FRIENDLY_ERROR_PAGES", True):
            return False
        if status_code not in {404, 500} or request.path.startswith("/api/"):
            return False
        accepted = request.headers.get("Accept", "text/html")
        return "text/html" in accepted or "*/*" in accepted
