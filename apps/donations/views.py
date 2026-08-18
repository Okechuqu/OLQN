from django.shortcuts import render


def give(request):
    return render(request, "donations/give.html")
