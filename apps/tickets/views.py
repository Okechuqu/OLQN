from django.http import HttpResponse


def my_tickets(request):
    return HttpResponse("Ticket access will be available after authentication.", status=501)
