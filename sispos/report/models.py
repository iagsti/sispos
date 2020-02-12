from django.db import models
from sispos.report.choices import RELATORES, ORIENTADORES, PROGRAMA, SEMESTRE
from uuid import uuid4
from sispos.accounts.models import User


class Report(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField('uuid', default=uuid4, editable=False)

    def get_absolute_url(self):
        return '/report/%s' % str(self.uuid)
        
    
    class Meta:
        verbose_name = 'relatório'
        verbose_name_plural = 'relatórios'

    def __str__(self):
        return self.aluno.name


class Semestre(models.Model):
    semestre = models.CharField(
        name='semestre',
        choices=SEMESTRE, max_length=50)
    relator = models.CharField(
        name='relator',
        choices=RELATORES, max_length=50)
    orientador = models.CharField(
        name='orientador',
        choices=ORIENTADORES, max_length=50)
    programa = models.CharField(
        name='programa',
        choices=PROGRAMA, max_length=50)
    relatorio = models.FileField(
        name='relatorio',
        upload_to='relatorios/%Y/%m/%d/')
    encaminhamento = models.FileField(
        name='encaminhamento',
        upload_to='encamnhamentos/%Y/%m/%d/')
    report = models.ForeignKey(
        'Report',
        on_delete=models.CASCADE)

    def get_absolute_url(self):
        return '/report/semestre/%s' % self.pk


class ParecerOrientadorMestrado(models.Model):
    s1_desempenho = models.TextField(
        'desempenho das disciplinas',
        max_length=2048)
    s1_projeto = models.TextField(
        'projeto de pesquisa',
        max_length=2048)
    s1_outras_atividades = models.TextField(
        'outras atividades',
        max_length=2048)
    s2_desempenho = models.TextField(
        'desempenho das disciplinas',
        max_length=2048, blank=True)
    s2_metodologia = models.TextField(
        'texto sobre a metodologia de trabalho',
        max_length=2048, blank=True)
    s2_abordagem = models.TextField(
        'Abordagem do problema a ser investigado',
        max_length=2048, blank=True)
    s2_outras_atividades = models.TextField(
        'Outras Atividades',
        max_length=2048, blank=True)
    s3_resultados = models.TextField(
        'resultados',
        max_length=2048, blank=True)
    s3_perspectivas = models.TextField(
        'perspectivas para a conclusão da dissertação',
        max_length=2048, blank=True)
    s3_resumo = models.TextField(
        'resumo expandido',
        max_length=2048, blank=True)
    s3_outras_atividades = models.TextField(
        'outras atividades',
        max_length=2048, blank=True)
    report = models.OneToOneField(
        'Report',
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        'criado em',
        auto_now_add=True)
    updated_at = models.DateTimeField(
        'atualizado em',
        auto_now=True)

    class Meta:
        verbose_name = 'parecer do orientador - mestrado'
        verbose_name_plural = 'pareceres dos orientadores - mestrados'
