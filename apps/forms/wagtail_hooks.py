from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

from apps.parish.models import ContactSubmission

ContactSubmission.panels = [
    FieldPanel("name", read_only=True),
    FieldPanel("email", read_only=True),
    FieldPanel("phone", read_only=True),
    FieldPanel("subject", read_only=True),
    FieldPanel("message", read_only=True),
    FieldPanel("created_at", read_only=True),
]
register_snippet(ContactSubmission)
