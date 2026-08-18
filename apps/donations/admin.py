from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

from .models import Donation

Donation.panels = [
    FieldPanel("donor_name"), FieldPanel("email"), FieldPanel("purpose"),
    FieldPanel("amount", read_only=True), FieldPanel("status", read_only=True),
    FieldPanel("reference", read_only=True),
]
register_snippet(Donation)
