from django.test import TestCase
from django.shortcuts import resolve_url as r
from sispos.report.forms import ParecerOrientadorMestradoForm

class ParecerOrientadorMestradoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('report:parecer_orientador_mestrado'))

    def test_status_code(self):
        """Status code must be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """It must render parecer_orientador_mestrado.html"""
        self.assertTemplateUsed(self.resp, 'parecer_orientador_mestrado.html')

    def test_inherite_main_template(self):
        """It must inherite main.html template"""
        self.assertTemplateUsed(self.resp, 'main.html')

    def test_template_title(self):
        """Template must contain title"""
        self.assertContains(self.resp, 'Parecer Orientador Mestrado')

    def test_context(self):
        """Context must has parecer_orientador_mestrado_form"""
        context = self.resp.context['form']
        self.assertIsInstance(context, ParecerOrientadorMestradoForm)

    def test_html(self):
        """Template must contain form html tags"""
        content = (
            (1, '<form'),
            (10, '<textarea'),
            (1, 'type="text"'),
            (1, '<button')
        )

        for count, expected in content:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def test_csrf(self):
        """Template must contain csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

