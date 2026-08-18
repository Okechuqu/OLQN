from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.images import get_image_model_string
from wagtail.models import Page


class HomePage(Page):
    template = "home/home_page.html"
    max_count = 1

    eyebrow = models.CharField(max_length=80, default="Welcome home")
    hero_title = models.CharField(max_length=180, default="Mary, Our Queen. Christ, Our King.")
    hero_text = models.TextField(
        default="A community of faith, love and service, rooted in the Eucharist and devoted to Our Lady."
    )
    hero_image = models.ForeignKey(
        get_image_model_string(), null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )
    welcome = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("eyebrow"),
                FieldPanel("hero_title"),
                FieldPanel("hero_text"),
                FieldPanel("hero_image"),
            ],
            heading="Hero",
        ),
        FieldPanel("welcome"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        from apps.events.models import EventPage
        from apps.news.models import AnnouncementPage, BulletinPage
        from apps.parish.models import MinistryPage

        context.update(
            events=EventPage.objects.live().public().order_by("start_at")[:3],
            announcements=AnnouncementPage.objects.live().public().order_by("-published_at")[:3],
            ministries=MinistryPage.objects.live().public()[:5],
            latest_bulletin=BulletinPage.objects.live().public().order_by("-bulletin_date").first(),
        )
        return context
