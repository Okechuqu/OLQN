import uuid

from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.images import get_image_model_string
from wagtail.models import Page


class EventIndexPage(Page):
    intro = models.TextField(blank=True)
    subpage_types = ["events.EventPage"]
    content_panels = Page.content_panels + [FieldPanel("intro")]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["events"] = EventPage.objects.child_of(
            self).live().public().order_by("start_at")
        return context


class EventPage(Page):
    start_at = models.DateTimeField(db_index=True)
    end_at = models.DateTimeField(null=True, blank=True)
    venue = models.CharField(max_length=180)
    body = RichTextField(blank=True)
    image = models.ForeignKey(
        get_image_model_string(), null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )
    capacity = models.PositiveIntegerField(null=True, blank=True)
    ticket_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    featured = models.BooleanField(default=False, db_index=True)
    content_panels = Page.content_panels + [
        FieldPanel("start_at"), FieldPanel(
            "end_at"), FieldPanel("venue"), FieldPanel("body"),
        FieldPanel("image"), FieldPanel("capacity"), FieldPanel(
            "ticket_price"), FieldPanel("featured"),
    ]


class Registration(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        PAID = "paid", "Paid"
        CANCELLED = "cancelled", "Cancelled"

    reference = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False)
    event = models.ForeignKey(
        EventPage, on_delete=models.PROTECT, related_name="registrations")
    name = models.CharField(max_length=160)
    email = models.EmailField()
    quantity = models.PositiveSmallIntegerField(default=1)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(
        max_length=12, choices=Status.choices, default=Status.PENDING, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
