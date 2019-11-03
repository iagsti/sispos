from django.test import TestCase
from sispos.report.models import Report
import uuid

class TestReportModel(TestCase):
    def setUp(self):
        self.obj = Report(
            relator='Relator 1',
            orientador='Orientador 1',
            programa='Programa 1',
            relatorio='relatorio.pdf',
            encaminhamento='encaminhamento.pdf'
        )
        self.obj.save()
    
    def test_model(self):
        """Must be a instance of Report"""
        self.assertIsInstance(self.obj, Report)

    def test_create(self):
        """Object must exists"""
        self.assertTrue(Report.objects.exists())

    def test_uuid(self):
        self.assertIsInstance(self.obj.uuid, uuid.UUID)