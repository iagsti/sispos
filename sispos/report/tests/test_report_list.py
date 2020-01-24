from unittest.mock import MagicMock
from django.core.files import File
from django.db.models.fields.files import FieldFile
from django.shortcuts import resolve_url as r
from django.test import TestCase

from sispos.accounts.models import User
from sispos.report.models import ParecerOrientadorMestrado, Report, Semestre


class ReportListTest(TestCase):
    def setUp(self):
        aluno = User.objects.create_user(
            login='123456', name='Stephen Pilsen',
            type='I',
            main_email='crises@tempest.com')
        report = Report.objects.create(aluno=aluno)

        relatorio = MagicMock(spec=File)
        relatorio.name = 'relatório.pdf'
        encaminhamento = MagicMock(spec=File)
        encaminhamento.name = 'encaminhamento.pdf'

        Semestre.objects.create(semestre='Primeiro Semestre',
                                relator='Relator 1',
                                programa='Mestrado',
                                relatorio=relatorio,
                                encaminhamento=encaminhamento,
                                report=report)
        ParecerOrientadorMestrado.objects.create(
            s1_desempenho='atisfatório',
            s1_projeto='Chimical churros analises',
            s1_outras_atividades='Nop',
            report=report)

        self.resp = self.client.get(r('report:report_list'))

    def test_url(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'report_list.html')

    def test_inherite_main_template(self):
        """It should inherite main.html template"""
        self.assertTemplateUsed(self.resp, 'main.html')

    def test_page_title(self):
        """Page must contain its title"""
        self.assertContains(self.resp, 'Relatórios')

    def test_template_list_header(self):
        """Report list must contains the correct header content"""
        header = ('Aluno', 'Programa', 'Relatório',
                  'Encaminhamento', 'Parecer')

        for expected in header:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_context(self):
        """Report context must show the correct content"""
        relatorio = MagicMock(spec=File)
        relatorio.name = 'relatorio.pdf'
        encaminhamento = MagicMock(spec=File)
        encaminhamento.name = 'encaminhamento.pdf'
        list_content = {
            'aluno': 'Stephen Pilsen',
            'programa': 'Mestrado',
            'report': relatorio,
            'encaminhamento': encaminhamento,
            'parecer': 1
        }

        report = Report.objects.get(pk=1)
        semestre = report.semestre_set.get(pk=1)
        parecer = report.parecerorientadormestrado.pk

        self.assertEqual(list_content['aluno'], report.aluno.get_full_name())
        self.assertEqual(list_content['programa'], semestre.programa)
        self.assertIsInstance(semestre.encaminhamento, FieldFile)
        self.assertIsInstance(semestre.relatorio, FieldFile)
        self.assertEqual(list_content['parecer'], parecer)

    def test_html_list_content(self):
        """Report list must show the correct content"""
        report = Report.objects.first()
        semestre = report.semestre_set.first()
        relatorio_url = semestre.relatorio.url
        encaminahmento_url = semestre.encaminhamento.url
        parecer = 'href="%s/parecer-orientador-mestrado"' % report.get_absolute_url()

        content = (
            'Stephen Pilsen',
            'Mestrado',
            relatorio_url,
            encaminahmento_url,
            parecer
        )

        for expected in content:
            with self.subTest():
                self.assertContains(self.resp, expected)
