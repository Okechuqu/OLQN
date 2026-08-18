from django.core.management.base import BaseCommand
from django.db import transaction
from wagtail.models import Page, Site

from apps.bulletins.models import BulletinIndexPage
from apps.events.models import EventIndexPage
from apps.home.models import HomePage
from apps.parish.models import AboutPage, ContactPage, MassTimesPage, MinistryIndexPage


class Command(BaseCommand):
    help = "Create the initial OLQN homepage and point the default Wagtail site to it."

    @transaction.atomic
    def handle(self, *args, **options):
        root = Page.get_first_root_node()
        homepage = HomePage.objects.first()

        if homepage is None:
            homepage = HomePage(
                title="Home",
                slug="olqn-home",
                eyebrow="Welcome home",
                hero_title="Mary, Our Queen. Christ, Our King.",
                hero_text=(
                    "A community of faith, love and service, rooted in the Eucharist "
                    "and devoted to Our Lady."
                ),
            )
            root.add_child(instance=homepage)
            homepage.save_revision().publish()
            self.stdout.write(self.style.SUCCESS("Created the OLQN homepage."))

        site, _ = Site.objects.get_or_create(
            hostname="localhost",
            defaults={"port": 80, "site_name": "OLQN Pro-Cathedral", "is_default_site": True},
        )
        site.root_page = homepage
        site.site_name = "OLQN Pro-Cathedral"
        site.is_default_site = True
        site.save()
        self.create_page(
            homepage,
            AboutPage,
            slug="about",
            title="About OLQN",
            intro=(
                "We are a community of faith in the heart of Abuja, dedicated to "
                "encountering Christ, growing in holiness, and serving with love."
            ),
            body=(
                "Our Lady Queen of Nigeria Catholic Pro-Cathedral, Garki, Abuja, is a "
                "spiritual home for Catholics in the Federal Capital Territory. As a "
                "Pro-Cathedral, we support the mission of the Archbishop and serve as a "
                "sign of unity for the local Church."
            ),
        )
        self.create_page(
            homepage,
            MassTimesPage,
            slug="mass-times",
            title="Mass Times & Confession",
            intro=(
                "Come encounter Christ with us in the Eucharist and the Sacrament "
                "of Reconciliation."
            ),
        )
        self.create_page(
            homepage,
            MinistryIndexPage,
            slug="ministries",
            title="Parish Life & Community",
            intro=(
                "We are many parts, but one body in Christ. Discover a place to "
                "belong, serve and grow in faith."
            ),
        )
        self.create_page(
            homepage,
            BulletinIndexPage,
            slug="bulletin",
            title="Parish Bulletin",
            intro="Read weekly notices, liturgical information and news from our parish community.",
        )
        self.create_page(
            homepage,
            EventIndexPage,
            slug="events",
            title="Events Ticketing & Updates",
            intro=(
                "Register, buy tickets and stay updated on parish events, programmes "
                "and community gatherings."
            ),
        )
        self.create_page(
            homepage,
            ContactPage,
            slug="contact",
            title="Contact Us",
            intro=(
                "We would be glad to hear from you. Contact the parish office or "
                "plan your visit."
            ),
            body=(
                "The Pro-Cathedral is located in Garki Area 3, Abuja, with accessible "
                "entrances and on-site parking."
            ),
        )
        self.stdout.write(self.style.SUCCESS("OLQN homepage is now the default site root."))

    def create_page(self, parent, model, **fields):
        existing = model.objects.filter(slug=fields["slug"]).first()
        if existing:
            return existing
        page = model(**fields)
        parent.add_child(instance=page)
        page.save_revision().publish()
        self.stdout.write(self.style.SUCCESS(f"Created /{fields['slug']}/"))
        return page
