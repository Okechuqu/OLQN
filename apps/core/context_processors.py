from .models import SiteSettings


def site_chrome(request):
    return {"site_settings": SiteSettings.for_request(request)}
