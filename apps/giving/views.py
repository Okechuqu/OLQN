from django.shortcuts import render


def give(request):
    return render(request, "giving/give.html")
