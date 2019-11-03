from django.db import models
from django.urls import reverse
from sispos.report.choices import RELATORES, ORIENTADORES, PROGRAMA
from uuid import uuid4


class Report(models.Model):
    relator = models.CharField(name='relator', choices=RELATORES, max_length=50)
    orientador = models.CharField(name='orientador', choices=ORIENTADORES, max_length=50)
    programa = models.CharField(name='programa', choices=PROGRAMA, max_length=50)
    relatorio = models.FileField(name='relatorio', upload_to='relatorios/%Y/%m/%d/')
    encaminhamento = models.FileField(name='encaminhamento', upload_to='encamnhamentos/%Y/%m/%d/')
    uuid = models.UUIDField('uuid', default=uuid4, editable=False)