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