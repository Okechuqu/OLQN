from django.http import HttpResponse


def index(request):
    return HttpResponse("Reports are available to authorised staff.")
