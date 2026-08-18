from django.contrib import messages
from django.db import models
from django.shortcuts import redirect
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.images import get_image_model_string
from wagtail.models import Page


class StandardPage(Page):
    intro = models.TextField(blank=True)
    body = RichTextField(blank=True)
    hero_image = models.ForeignKey(
        get_image_model_string(), null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )
    content_panels = Page.content_panels + [
        FieldPanel("intro"), FieldPanel("hero_image"), FieldPanel("body")
    ]


class AboutPage(StandardPage):
    template = "parish/about_page.html"
    max_count = 1


class MassTimesPage(StandardPage):
    template = "parish/mass_times_page.html"
    max_count = 1


class ContactPage(StandardPage):
    template = "parish/contact_page.html"
    max_count = 1

    def serve(self, request, *args, **kwargs):
        if request.method == "POST":
            required = [
                request.POST.get("name", "").strip(),
                request.POST.get("email", "").strip(),
                request.POST.get("message", "").strip(),
            ]
            if all(required):
                ContactSubmission.objects.create(
                    name=required[0],
                    email=required[1],
                    phone=request.POST.get("phone", "").strip(),
                    subject=request.POST.get("subject", "General enquiry").strip(),
                    message=required[2],
                )
                messages.success(
                    request, "Thank you. Your message has been sent to the parish office."
                )
                return redirect(self.url)
            messages.error(request, "Please complete your name, email and message.")
        return super().serve(request, *args, **kwargs)


class ContactSubmission(models.Model):
    name = models.CharField(max_length=160)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    subject = models.CharField(max_length=120)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}: {self.subject}"


class MinistryIndexPage(StandardPage):
    subpage_types = ["parish.MinistryPage"]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["ministries"] = MinistryPage.objects.child_of(self).live().public()
        return context


class MinistryPage(StandardPage):
    meeting_time = models.CharField(max_length=140, blank=True)
    contact_email = models.EmailField(blank=True)
    content_panels = StandardPage.content_panels + [
        FieldPanel("meeting_time"), FieldPanel("contact_email")
    ]
