from django.test import TestCase, Client

# Create your tests here.
class AppTest(TestCase):
    def katalog_url_exists(self):
        response = Client().get('/katalog/')
        self.assertEqual(response.status_code, 200)

    def katalog_template_test(self):
        response = Client().get('/katalog/')
        self.assertTemplateUsed(response, 'katalog.html')