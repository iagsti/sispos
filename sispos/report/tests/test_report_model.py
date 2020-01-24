from django.test import TestCase
from sispos.report.models import Report
from sispos.accounts.models import User
import uuid

class TestReportModel(TestCase):
    def setUp(self):
        aluno = User.objects.create_user(
            login='3544444',
            main_email='main@test.com',
            password='92874',
            name='Marc',
            type='I'
        )

        self.obj = Report(
            aluno=aluno
        )
        self.obj.save()
    
    def test_model(self):
        """Must be a instance of Report"""
        self.assertIsInstance(self.obj, Report)

    def test_create(self):
        """Object must exists"""
        self.assertTrue(Report.objects.exists())

    def test_uuid(self):
        """Must contain uuid field"""
        self.assertIsInstance(self.obj.uuid, uuid.UUID)

    def test_aluno(self):
        """It must has aluno field"""
        self.assertIsInstance(self.obj.aluno, User)
        
    def test_str(self):
        self.assertEqual('Marc', str(self.obj))

    def test_get_absolute_id(self):
        expected = '/report/%s' % str(self.obj.uuid)
        self.assertEqual(expected, self.obj.get_absolute_url())

