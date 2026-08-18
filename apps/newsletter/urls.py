from django.urls import path

from .views import subscribe_view

app_name = "newsletter"
urlpatterns = [path("", subscribe_view, name="subscribe")]
