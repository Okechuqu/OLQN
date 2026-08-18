from django.core.management import call_command
from django.test import RequestFactory, TestCase, override_settings

from apps.core.error_views import server_error
from apps.events.models import EventPage, Registration
from apps.parish.models import ContactSubmission


class PublicNavigationTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("bootstrap_site", verbosity=0)

    def test_all_primary_navigation_pages_render(self):
        for path in [
            "/",
            "/about/",
            "/leadership/",
            "/mass-times/",
            "/sacraments/",
            "/sacraments/baptism/",
            "/sacraments/matrimony/",
            "/sacraments/confirmation/",
            "/ministries/",
            "/ministries/cyon/",
            "/ministries/cwo/",
            "/ministries/cmo/",
            "/bulletins/",
            "/bulletins/latest-parish-bulletin/",
            "/announcements/",
            "/announcements/welcome-to-olqn-updates/",
            "/events/",
            "/events/parish-family-day/",
            "/events/parish-family-day/register/",
            "/events/parish-family-day/tickets/",
            "/tickets/",
            "/tickets/verify/",
            "/give/",
            "/projects/",
            "/projects/parish-development/",
            "/gallery/",
            "/watch-live/",
            "/contact/",
            "/search/",
        ]:
            with self.subTest(path=path):
                response = self.client.get(path, HTTP_HOST="localhost")
                self.assertEqual(response.status_code, 200)

    def test_contact_form_stores_an_enquiry(self):
        response = self.client.post(
            "/contact/",
            {
                "name": "Ada Visitor",
                "email": "ada@example.com",
                "subject": "General enquiry",
                "message": "Please share the parish office hours.",
            },
            HTTP_HOST="localhost",
        )
        self.assertRedirects(response, "/contact/", fetch_redirect_response=False)
        self.assertTrue(ContactSubmission.objects.filter(email="ada@example.com").exists())

    def test_event_registration_and_ticket_detail_routes(self):
        event = EventPage.objects.get(slug="parish-family-day")
        response = self.client.post(
            f"/events/{event.slug}/register/",
            {"name": "Ada Visitor", "email": "ada@example.com", "quantity": 2},
            HTTP_HOST="localhost",
        )
        registration = Registration.objects.get(email="ada@example.com")
        self.assertRedirects(
            response,
            f"/tickets/{registration.reference}/",
            fetch_redirect_response=False,
        )
        detail = self.client.get(
            f"/tickets/{registration.reference}/", HTTP_HOST="localhost"
        )
        self.assertEqual(detail.status_code, 200)

    @override_settings(DEBUG=False)
    def test_custom_404_page(self):
        response = self.client.get("/this-page-does-not-exist/", HTTP_HOST="localhost")
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "Page not found", status_code=404)

    @override_settings(DEBUG=True, FRIENDLY_ERROR_PAGES=True)
    def test_debug_mode_uses_branded_404_for_browser_requests(self):
        response = self.client.get(
            "/not-pages/", HTTP_HOST="localhost", HTTP_ACCEPT="text/html"
        )
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "Page not found", status_code=404)
        self.assertNotContains(response, "Using the URLconf", status_code=404)

    def test_custom_500_page(self):
        request = RequestFactory().get("/")
        response = server_error(request)
        self.assertEqual(response.status_code, 500)
        self.assertContains(response, "We’ll be back shortly", status_code=500)

    @override_settings(
        DEBUG=True,
        FRIENDLY_ERROR_PAGES=True,
        ROOT_URLCONF="apps.core.test_urls",
    )
    def test_debug_mode_hides_exception_behind_branded_500(self):
        self.client.raise_request_exception = False
        response = self.client.get(
            "/server-error/", HTTP_HOST="localhost", HTTP_ACCEPT="text/html"
        )
        self.assertEqual(response.status_code, 500)
        self.assertContains(response, "We’ll be back shortly", status_code=500)
        self.assertNotContains(response, "RuntimeError", status_code=500)
