from django.test import TestCase
from django.shortcuts import resolve_url as r


class MainPageTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_url(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_extend_main_template(self):
        self.assertTemplateUsed(self.resp, 'main.html')

    def test_nav_bar(self):
        """Main page should contain a nav bar"""
        self.assertContains(self.resp, '<nav')

    def test_start_button(self):
        """Main page should contain a link to login"""
        self.assertContains(self.resp, r('accounts:login'))
