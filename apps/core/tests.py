from django.core.management import call_command
from django.test import TestCase

from apps.parish.models import ContactSubmission


class PublicNavigationTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("bootstrap_site", verbosity=0)

    def test_all_primary_navigation_pages_render(self):
        for path in [
            "/",
            "/about/",
            "/mass-times/",
            "/ministries/",
            "/bulletin/",
            "/events/",
            "/give/",
            "/contact/",
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
