from django.test import TestCase
from sispos.report.models import Semestre, Report
from sispos.accounts.models import User


class SemestreModelTest(TestCase):
    def setUp(self):
        self.create_report()

    def test_model(self):
        self.assertTrue(Semestre.objects.exists())

    def test_report(self):
        self.assertIsInstance(self.obj.report, Report)

    def test_absolute_url(self):
        url = self.obj.get_absolute_url()
        self.assertEqual(url, '/report/semestre/%s' % self.obj.pk)

    def test_custom_semestre_permissions(self):
        permissions = Semestre._meta.permissions
        expected = [('change_semestre_relator', 'Can change semestre relator')]
        self.assertListEqual(expected, permissions)

    def create_report(self):
        user = User.objects.create_user(
            login='3544444',
            main_email='main@test.com',
            password='92874',
            name='Marc',
            type='I'
        )

        report = Report.objects.create(aluno=user)

        self.obj = Semestre.objects.create(
            semestre='Primeiro Semestre',
            relator='Relator 1',
            orientador='Orientador 1',
            programa='Programa 1',
            relatorio='relatorio.pdf',
            encaminhamento='encaminhamento.pdf',
            report=report
        )
