from django.test import TestCase
from sispos.report.forms import ParecerOrientadorMestradoForm

class ParecerFormTest(TestCase):
    def setUp(self):
        self.form = ParecerOrientadorMestradoForm()
    
    def test_fields(self):
        """Form should contain fields"""
        itens = ['s1_desempenho', 's1_projeto', 's1_outras_atividades',
                's2_desempenho', 's2_metodologia', 's2_abordagem', 's2_outras_atividades',
                's3_resultados', 's3_perspectivas', 's3_resumo', 's3_outras_atividades', 'report']
        for expected in itens:
            with self.subTest():
                self.assertIn(expected, list(self.form.fields))

    def test_fields_not_required(self):
        """Related fields must not be required"""
        not_required = ['s2_desempenho', 's2_metodologia', 's2_abordagem', 's2_outras_atividades',
                        's3_resultados', 's3_perspectivas', 's3_resumo', 's3_outras_atividades']

        for field in not_required:
            with self.subTest():
                self.assertFalse(self.form.fields[field].required)