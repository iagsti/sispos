from django.test import TestCase
from sispos.report.forms import ReportForm

class TestReportForm(TestCase):
    def setUp(self):
        self.form = ReportForm()

    def test_form(self):
        expected = ['relator', 'orientador', 'programa', 'relatorio', 'encaminhamento']
        self.assertSequenceEqual(expected, list(self.form.fields))