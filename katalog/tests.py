from django.test import TestCase, Client

# Create your tests here.
class KatalogTest(TestCase):
    def test_katalog_url_exists(self):
        response = Client().get('/katalog/')
        self.assertEqual(response.status_code, 200)