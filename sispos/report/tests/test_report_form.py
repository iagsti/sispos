from django.test import TestCase
from sispos.report.forms import ReportForm

class TestReportForm(TestCase):
    def setUp(self):
        self.form = ReportForm()

    def test_form(self):
        fields = ['relator', 'orientador', 'programa', 'relatorio', 'encaminhamento']

        for expected in fields:
            with self.subTest():
                self.assertIn(expected, list(self.form.fields))

    def test_semestre(self):
        self.assertIn('semestre', list(self.form.fields))