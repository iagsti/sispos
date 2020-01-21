from django.test import TestCase
from django.shortcuts import resolve_url as r


class ReportViewParecerPostTest(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('report:parecer_orientador_mestrado'))
