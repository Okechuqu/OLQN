from django.urls import path

from .views import my_tickets

app_name = "tickets"
urlpatterns = [path("", my_tickets, name="mine")]
