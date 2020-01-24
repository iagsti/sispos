from django.test import TestCase
from django.shortcuts import resolve_url as r
from sispos.report.forms import ParecerOrientadorMestradoForm
from sispos.report.models import Report, ParecerOrientadorMestrado
from sispos.accounts.models import User


class ParecerOrientadorMestradoTestGet(TestCase):
    def setUp(self):
        aluno = User.objects.create_user(login='3544444', main_email='main@test.com',
                                        password='92874', name='Marc', type='I')
        
        report = Report.objects.create(aluno=aluno)
        self.report_uuid = report.uuid
        self.resp = self.client.get(r('report:parecer_orientador_mestrado', slug=report.uuid))

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
            (1, '<button'),
            (2, 'type="hidden"'),
            (1, 'no-validate')
        )

        for count, expected in content:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def test_csrf(self):
        """Template must contain csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_report_field_content(self):
        """report field must be filled with uuid report"""
        expected = 'value="%s"' % self.report_uuid
        self.assertContains(self.resp, expected)


class ParecerOrientadorMestradoTestPost(TestCase):
    def setUp(self):
        data = self.make_parecer()
        self.resp = self.client.post(r('report:parecer_orientador_mestrado_create'), data)

    def test_status_code(self):
        """Status code must be 200"""
        self.assertEqual(302, self.resp.status_code)

    def test_parecer_saved(self):
        """Parecer should be saved"""
        self.assertEqual(ParecerOrientadorMestrado.objects.count(), 1)

    def make_parecer(self, **kwargs):
        aluno = User.objects.create_user(login='3544444', main_email='main@test.com',
                                        password='92874', name='Marc', type='I')

        report = Report.objects.create(aluno=aluno)
        parecer_default = dict(s1_desempenho='Desempenho', s1_projeto='Projeto',
                          s1_outras_atividades='Outras atividades', report=report.uuid)

        parecer = dict(parecer_default, **kwargs)

        return parecer

