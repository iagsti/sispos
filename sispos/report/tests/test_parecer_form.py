from django.test import TestCase
from sispos.report.forms import ParecerOrientadorMestradoForm

class ParecerFormTest(TestCase):
    def setUp(self):
        self.form = ParecerOrientadorMestradoForm()
    
    def test_fields(self):
        """Form should contain fields"""
        itens = ['s1_desempenho', 's1_projeto', 's1_outras_atividades',
                's2_desempenho', 's2_metodologia', 's2_abordagem', 's2_outras_atividades',
                's3_resultados', 's3_perspectivas', 's3_resumo', 's3_outras_atividades']
        for expected in itens:
            with self.subTest():
                self.assertIn(expected, list(self.form.fields))
