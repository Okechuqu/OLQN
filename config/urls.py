from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from django.views.generic import RedirectView
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

handler404 = "apps.core.error_views.page_not_found"
handler500 = "apps.core.error_views.server_error"

urlpatterns = [
    path("health/", lambda request: JsonResponse({"status": "ok"}), name="health"),
    path("django-admin/", admin.site.urls),
    path("cms/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("api/payments/", include("apps.payments.urls", namespace="payments")),
    path("events/", include("apps.events.urls", namespace="events")),
    path("tickets/", include("apps.tickets.urls", namespace="tickets")),
    path("newsletter/", include("apps.newsletter.urls", namespace="newsletter")),
    path("give/", include("apps.donations.urls", namespace="giving")),
    path("search/", include("apps.core.search_urls", namespace="search")),
    path("bulletin/", RedirectView.as_view(url="/bulletins/", permanent=True)),
    path("", include(wagtail_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
