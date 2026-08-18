from django.shortcuts import render
from wagtail.models import Page


def search(request):
    query = request.GET.get("q", "").strip()
    results = Page.objects.none()
    if query:
        results = Page.objects.live().public().search(query)
    return render(request, "search.html", {"query": query, "results": results})
