from django.test import TestCase
from sispos.report.models import ParecerOrientadorMestrado, Report
from sispos.accounts.models import User
from datetime import datetime


class ReportParecerOrientadorMestradoTest(TestCase):
    def setUp(self):
        report = self.create_report()
        self.obj = ParecerOrientadorMestrado.objects.create(
            s1_desempenho='Desempenho bom',
            s1_projeto='Projeto de pesquisa teste',
            s1_outras_atividades='Outras atividades desempehnadas',
            s2_desempenho='Desempenho bom do semestre 2',
            s2_metodologia='Metodologia para o trabalho',
            s2_abordagem='Abordagem do problema a ser investigado',
            s2_outras_atividades='Outras atividades desempenhadas',
            s3_resultados='Resultados preliminares',
            s3_perspectivas='Perspectivas para a conclusão do da dissertação',
            s3_resumo='Resumo Expandido',
            s3_outras_atividades='Outras atividades desempenhadas',
            report=report
        )

    def test_parecer_orientador_mestrado(self):
        """It must be an instance of ParecerOrientadorMestrado"""
        self.assertIsInstance(self.obj, ParecerOrientadorMestrado)

    def test_create(self):
        """It must exists no database"""
        self.assertTrue(ParecerOrientadorMestrado.objects.exists())

    def test_report(self):
        """It must have report attribute"""
        report = ParecerOrientadorMestrado.report
        self.assertNotEqual(report, None)

    def test_report_instance(self):
        """It must be an Report instance"""
        self.assertIsInstance(self.obj.report, Report)

    def test_created_at(self):
        """It must have a created_at attribute"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_updated_at(self):
        """It must have a updated_at attribute"""
        self.assertIsInstance(self.obj.updated_at, datetime)
    
    def test_not_required(self):
        """Require must be false"""
        blank_set = ['s2_desempenho', 's2_metodologia', 's2_abordagem', 's2_outras_atividades',
                    's3_resultados', 's3_perspectivas', 's3_resumo', 's3_outras_atividades']
        for expected in blank_set:
            with self.subTest():
                self.assertIsBlank(ParecerOrientadorMestrado, expected)

    def assertIsBlank(self, obj, parameter):
        p_instance = getattr(obj, parameter)
        self.assertTrue(p_instance.field.blank)

    def create_report(self):
        user = User.objects.create_user(
            login='3544444',
            main_email='main@test.com',
            password='92874',
            name='Marc',
            type='I'
        )

        return user.report_set.create(
            aluno=user
        )


