from django.urls import path

from . import views

app_name = "giving"
urlpatterns = [path("", views.give, name="give")]
