from django.test import TestCase
from sispos.report.admin import ReportModelAdmin
from sispos.report.models import Report
from sispos.accounts.models import User
from unittest import mock
from django.core.files import File
from django.contrib import admin


class ReportAdminTest(TestCase):
    def test_list_display(self):
        list = ['aluno_name']

        for expected in list:
            with self.subTest():
                self.assertIn(expected, ReportModelAdmin.list_display)

    def test_name_aluno(self):
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'test.pdf'
        
        aluno = User.objects.create_user(
            login='3544444',
            main_email='main@test.com',
            password='92874',
            name='Marc',
            type='I'
        )

        report = Report.objects.create(
            aluno=aluno
        )

        name = ReportModelAdmin(Report, admin.site).aluno_name(obj=report)
        self.assertEqual(name, aluno.get_full_name())