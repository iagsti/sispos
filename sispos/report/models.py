from django.db import models
from django.urls import reverse
from sispos.report.choices import RELATORES, ORIENTADORES, PROGRAMA
from uuid import uuid4
from sispos.accounts.models import User


class Report(models.Model):
    relator = models.CharField(name='relator', choices=RELATORES, max_length=50)
    orientador = models.CharField(name='orientador', choices=ORIENTADORES, max_length=50)
    programa = models.CharField(name='programa', choices=PROGRAMA, max_length=50)
    relatorio = models.FileField(name='relatorio', upload_to='relatorios/%Y/%m/%d/')
    encaminhamento = models.FileField(name='encaminhamento', upload_to='encamnhamentos/%Y/%m/%d/')
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField('uuid', default=uuid4, editable=False)

    class Meta:
        verbose_name = 'relatório'
        verbose_name_plural = 'relatórios'

    def __str__(self):
        return self.aluno.name


class ParecerOrientadorMestrado(models.Model):
    s1_desempenho = models.CharField('desempenho das disciplinas', max_length=2048)
    s1_projeto = models.CharField('projeto de pesquisa', max_length=2048)
    s1_outras_atividades = models.CharField('outras atividades', max_length=2048)
    s2_desempenho = models.CharField('desempenho das disciplinas', max_length=2048)
    s2_metodologia = models.CharField('texto sobre a metodologia de trabalho', max_length=2048)
    s2_abordagem = models.CharField('Abordagem do problema a ser investigado', max_length=2048)
    s2_outras_atividades = models.CharField('Outras Atividades', max_length=2048)
    s3_resultados = models.CharField('resultados', max_length=2048)
    s3_perspectivas = models.CharField('perspectivas para a conclusão da dissertação', max_length=2048)
    s3_resumo = models.CharField('resumo expandido', max_length=2048)
    s3_outras_atividades = models.CharField('outras atividades', max_length=2048)
    report = models.OneToOneField('Report', on_delete=models.CASCADE)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'parecer do orientador - mestrado'
        verbose_name_plural = 'pareceres dos orientadores - mestrados'

        
    def __str__(self):
        return self.report.orientador
