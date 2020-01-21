from django.test import TestCase
from django.shortcuts import resolve_url as r
from sispos.accounts.models import User


class AccountsTemplateTest(TestCase):
    def setUp(self):
        user = self.make_user()
        self.client.force_login(user)
        self.resp = self.client.get(r('accounts:user'))

    def test_status(self):
        """Status code must be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """It should use user.html template"""
        self.assertTemplateUsed(self.resp, 'user.html')

    def test_inherite_main_template(self):
        """It should inherite main.html template"""
        self.assertTemplateUsed(self.resp, 'main.html')

    def test_page_title(self):
        """It should contain the page title"""
        self.assertContains(self.resp, 'Dados do usuário')

    def make_user(self):
        user_data = {
            'login': '5554477',
            'name': 'Thomas Fullstack Python',
            'type': 'I',
            'main_email': 'thomas@test.com',
            'bond': "[{'tipoVinculo': 'SERVIDOR'}]"
        }

        user = User.objects.create_user(**user_data)
        return user
