from datetime import timedelta

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from wagtail.models import Page, Site

from apps.announcements.models import AnnouncementIndexPage
from apps.bulletins.models import AnnouncementPage, BulletinIndexPage, BulletinPage
from apps.clergy.models import LeadershipPage
from apps.events.models import EventIndexPage, EventPage
from apps.gallery.models import GalleryPage
from apps.home.models import HomePage
from apps.livestream.models import LivestreamPage
from apps.parish.models import (
    AboutPage,
    ContactPage,
    MassTimesPage,
    MinistryIndexPage,
    MinistryPage,
)
from apps.projects.models import ProjectIndexPage, ProjectPage
from apps.sacraments.models import SacramentIndexPage, SacramentPage


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
            LeadershipPage,
            slug="leadership",
            title="Parish Leadership",
            intro="Meet the clergy and pastoral leaders serving our parish community.",
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
        sacraments = self.create_page(
            homepage,
            SacramentIndexPage,
            slug="sacraments",
            title="The Sacraments",
            intro="Encounter Christ through the sacramental life of the Church.",
        )
        for slug, title, intro, preparation in [
            (
                "baptism",
                "Baptism",
                "Begin the Christian journey through water and the Holy Spirit.",
                "Contact the parish office to register for the preparation class.",
            ),
            (
                "matrimony",
                "Holy Matrimony",
                "Prepare to enter the covenant of Christian marriage.",
                "Contact the parish office at least six months before the proposed date.",
            ),
            (
                "confirmation",
                "Confirmation",
                "Receive the fullness of the gifts of the Holy Spirit.",
                "Candidates complete the approved parish formation programme.",
            ),
        ]:
            self.create_page(
                sacraments,
                SacramentPage,
                slug=slug,
                title=title,
                intro=intro,
                body=intro,
                preparation=preparation,
            )
        ministries = self.create_page(
            homepage,
            MinistryIndexPage,
            slug="ministries",
            title="Parish Life & Community",
            intro=(
                "We are many parts, but one body in Christ. Discover a place to "
                "belong, serve and grow in faith."
            ),
        )
        for slug, title, intro in [
            ("cyon", "CYON", "Catholic Youth Organisation of Nigeria."),
            ("cwo", "CWO", "Catholic Women Organisation."),
            ("cmo", "CMO", "Catholic Men Organisation."),
        ]:
            self.create_page(
                ministries, MinistryPage, slug=slug, title=title, intro=intro
            )
        bulletin_index = BulletinIndexPage.objects.first()
        if bulletin_index and bulletin_index.slug != "bulletins":
            bulletin_index.slug = "bulletins"
            bulletin_index.save_revision().publish()
        bulletins = self.create_page(
            homepage,
            BulletinIndexPage,
            slug="bulletins",
            title="Parish Bulletin",
            intro="Read weekly notices, liturgical information and news from our parish community.",
        )
        self.create_page(
            bulletins,
            BulletinPage,
            slug="latest-parish-bulletin",
            title="Latest Parish Bulletin",
            bulletin_date=timezone.localdate(),
            summary="The latest notices and liturgical information from OLQN.",
        )
        announcements = self.create_page(
            homepage,
            AnnouncementIndexPage,
            slug="announcements",
            title="Announcements & Updates",
            intro="Important notices and timely updates from the parish community.",
        )
        self.create_page(
            announcements,
            AnnouncementPage,
            slug="welcome-to-olqn-updates",
            title="Welcome to OLQN Updates",
            published_at=timezone.localdate(),
            body="Important parish announcements will be published here.",
        )
        events = self.create_page(
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
            events,
            EventPage,
            slug="parish-family-day",
            title="Parish Family Day",
            start_at=timezone.now() + timedelta(days=30),
            venue="Pro-Cathedral Grounds",
            body="A day of faith, fellowship and community for the whole parish.",
            ticket_price=0,
            featured=True,
        )
        projects = self.create_page(
            homepage,
            ProjectIndexPage,
            slug="projects",
            title="Parish Projects",
            intro="Together we build for worship, service and future generations.",
        )
        self.create_page(
            projects,
            ProjectPage,
            slug="parish-development",
            title="Parish Development",
            summary="Supporting facilities for worship, formation and community life.",
            body="Follow progress and support this parish development initiative.",
        )
        self.create_page(
            homepage,
            GalleryPage,
            slug="gallery",
            title="Parish Gallery",
            intro="Moments of worship, fellowship and service in our parish community.",
        )
        self.create_page(
            homepage,
            LivestreamPage,
            slug="watch-live",
            title="Watch Live",
            intro="Join Mass and special celebrations from OLQN Pro-Cathedral.",
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
