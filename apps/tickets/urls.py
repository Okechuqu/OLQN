from django.urls import path

from .views import my_tickets, ticket_detail, verify

app_name = "tickets"
urlpatterns = [
    path("", my_tickets, name="mine"),
    path("verify/", verify, name="verify"),
    path("<uuid:reference>/", ticket_detail, name="detail"),
]
