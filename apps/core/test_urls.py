from django.urls import path


def raise_server_error(request):
    raise RuntimeError("Intentional exception used to test the branded 500 page.")


urlpatterns = [path("server-error/", raise_server_error)]
