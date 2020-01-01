from django.test import TestCase
from django.core.files import File
from django.shortcuts import resolve_url as r
from sispos.report.models import ParecerOrientadorMestrado, Report, Semestre
from unittest.mock import MagicMock
from sispos.accounts.models import User


class ReportListTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('report:report_list'))

        aluno = User.objects.create_user(
            login='123456', name='Stephen Pilsen',
            type='I',
            main_email='crises@tempest.com')
        report = Report.objects.create(aluno=aluno)
        Semestre.objects.create(semestre='Primeiro Semestre',
                                relator='Relator 1',
                                programa='Mestrado',
                                relatorio='relatorio.pdf',
                                encaminhamento='encaminhamento.pdf',
                                report=report)
        ParecerOrientadorMestrado.objects.create(
            s1_desempenho='atisfatório',
            s1_projeto='Chimical churros analises',
            s1_outras_atividades='Nop',
            report=report)

    def test_url(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'report_list.html')

    def test_template_list_header(self):
        """Report list must contains the correct header content"""
        header = ('Aluno', 'Programa', 'Relatório', 'Parecer')

        for expected in header:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_list_content(self):
        """Report list must show the correct content"""
        file_mock = MagicMock(spec=File)
        file_mock.name = 'relatorio.pdf'
        list_content = {
            'aluno': 'Stephen Pilsen',
            'programa': 'Mestrado',
            'report': file_mock,
            'parecer': 1
        }

        report = Report.objects.get(pk=1)
        semestre = report.semestre_set.get(pk=1)
        parecer = report.parecerorientadormestrado.pk

        self.assertEqual(list_content['aluno'], report.aluno.get_full_name())
        self.assertEqual(list_content['programa'], semestre.programa)
        self.assertEqual(list_content['report'], semestre.relatorio)
        self.assertEqual(list_content['parecer'], parecer)
