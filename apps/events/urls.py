from django.urls import path

from . import views

app_name = "events"
urlpatterns = [
    path("<slug:event_slug>/register/", views.register, name="register"),
    path("<slug:event_slug>/tickets/", views.event_tickets, name="tickets"),
]
