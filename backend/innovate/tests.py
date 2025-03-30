from django.test import TestCase
from django.contrib.admin.sites import site
from .models import FeedBackRequest
from .admin import FeedBackRequestAdmin

class FeedBackRequestAdminTest(TestCase):
    def test_admin_registered(self):
        """Ensure FeedBackRequest is registered in Django Admin."""
        self.assertTrue(site.is_registered(FeedBackRequest))

    def test_admin_fields(self):
        """Ensure admin displays correct fields."""
        admin_instance = FeedBackRequestAdmin(FeedBackRequest, site)
        self.assertEqual(admin_instance.list_display, ("tags", "created_at"))

