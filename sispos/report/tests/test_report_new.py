from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.core.files import File
from sispos.report.forms import ReportForm
from sispos.report.models import Report, Semestre
from unittest import mock
from sispos.accounts.models import User


class TestReportNewGetLoggedIn(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            login='3544444',
            main_email='main@test.com',
            password='92874',
            name='Marc',
            type='I'
        )
        self.client.force_login(user)
        self.resp = self.client.get(r('report:new'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must render the new template"""
        self.assertTemplateUsed(self.resp, 'report_form.html')

    def test_html(self):
        """Must contain fields Relator=select, Orientador=select, Programa=select,
        Relatório=arquivo, Formulário de encaminhamento=arquivo"""
        expected = (
            ('<form', 1),
            ('<select', 4),
            ('<input', 3),
            ('<button', 1)
        )

        for item, count in expected:
            with self.subTest():
                self.assertContains(self.resp, item, count)

    def test_has_form(self):
        """Must be an instance of ReportForm"""
        form = self.resp.context['form']
        self.assertIsInstance(form, ReportForm)


class TestReportNewPost(TestCase):
    def setUp(self):
        aluno = User.objects.create_user(
            login='3544444',
            main_email='main@test.com',
            password='92874',
            name='Marc',
            type='I'
        )

        self.client.force_login(aluno)
        
        self.data = dict(
            semestre='Primeiro Semestre',
            relator='Relator 1',
            orientador='Orientador 1',
            programa='Mestrado',
            relatorio=mock.MagicMock(spec=File),
            encaminhamento=mock.MagicMock(spec=File),
        )
        self.resp = self.client.post(r('report:new'), self.data)
    
    def test_post(self):
        """Status code must be 302"""
        self.assertEqual(302, self.resp.status_code)

    def test_create(self):
        """Object must exists on database"""
        self.assertTrue(Report.objects.exists())

    def test_semestre(self):
        """Semestre must exists on database"""
        self.assertTrue(Semestre.objects.exists())

class TestNewGetAnonimous(TestCase):
    def test_redirect(self):
        """Anonimous must be redirected"""
        resp = self.client.get(r('report:new'))
        self.assertEqual(302, resp.status_code)