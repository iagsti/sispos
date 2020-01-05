from django.test import TestCase


class MainPageTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_url(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_extend_main_template(self):
        self.assertTemplateUsed(self.resp, 'main.html')