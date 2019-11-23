from django import forms
from sispos.report.choices import RELATORES, ORIENTADORES, PROGRAMA, SEMESTRE


class ReportForm(forms.Form):
    semestre = forms.ChoiceField(label='semestre', choices=SEMESTRE)
    relator = forms.ChoiceField(label='relator', choices=RELATORES)
    orientador = forms.ChoiceField(label='orientador', choices=ORIENTADORES)
    programa = forms.ChoiceField(label='programa', choices=PROGRAMA)
    relatorio = forms.FileField(label='relatorio')
    encaminhamento = forms.FileField(label='encaminhamento')
