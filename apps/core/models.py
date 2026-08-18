from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import RichTextField
from wagtail.images import get_image_model_string


@register_setting
class SiteSettings(BaseSiteSetting):
    logo = models.ForeignKey(
        get_image_model_string(), null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )
    parish_name = models.CharField(
        max_length=160, default="Our Lady Queen of Nigeria Catholic Pro-Cathedral"
    )
    location_label = models.CharField(max_length=80, default="Garki, Abuja")
    address = models.TextField(default="Ibadan Street, Garki Area 3, Abuja")
    phone = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)
    live_stream_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    footer_note = RichTextField(blank=True, features=["bold", "link"])

    panels = [
        MultiFieldPanel(
            [FieldPanel("logo"), FieldPanel("parish_name"), FieldPanel("location_label")],
            heading="Identity",
        ),
        MultiFieldPanel(
            [FieldPanel("address"), FieldPanel("phone"), FieldPanel("email")],
            heading="Contact",
        ),
        MultiFieldPanel(
            [
                FieldPanel("live_stream_url"),
                FieldPanel("facebook_url"),
                FieldPanel("instagram_url"),
                FieldPanel("youtube_url"),
            ],
            heading="Links",
        ),
        FieldPanel("footer_note"),
    ]
