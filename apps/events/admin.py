from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

from .models import Registration

Registration.panels = [
    FieldPanel("event"), FieldPanel("name"), FieldPanel("email"), FieldPanel("quantity"),
    FieldPanel("amount", read_only=True), FieldPanel("status", read_only=True),
    FieldPanel("reference", read_only=True),
]
register_snippet(Registration)
