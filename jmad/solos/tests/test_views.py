from django.test import TestCase, RequestFactory

from solos.views import index


class IndexViewTestCase(TestCase):

    def setUp(self):
        # RequestFactory is a tool for creating and fine-tuning
        # HTTP requests that we can use to test view functions.
        self.factory = RequestFactory()

    def test_index_view_basic(self):
        """
        Test that index view returns a 200 response and uses
        the correct template
        """
        request = self.factory.get('/')
        with self.assertTemplateUsed('solos/index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)
