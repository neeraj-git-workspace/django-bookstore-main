from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class SearchAjaxTestCase(TestCase):
    """
    AJAX Search View Test Case
    """

    def setUp(self):
        self.url = reverse("search_ajax")

    def test_search_ajax_view_status_code(self):
        """
        AJAX Test request with valid and invalid Book Name
        """
        response = self.client.post(
            self.url, data={"bookName": "Text"}, HTTP_X_REQUESTED_WITH="XMLHttpRequest"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("true", response.content.decode("utf-8"))

        response = self.client.post(
            self.url, data={}, HTTP_X_REQUESTED_WITH="XMLHttpRequest"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("false", response.content.decode("utf-8"))


