from django import forms
from sispos.report.choices import RELATORES, ORIENTADORES, PROGRAMA, SEMESTRE


class ReportForm(forms.Form):
    semestre = forms.ChoiceField(label='semestre', choices=SEMESTRE)
    relator = forms.ChoiceField(label='relator', choices=RELATORES)
    orientador = forms.ChoiceField(label='orientador', choices=ORIENTADORES)
    programa = forms.ChoiceField(label='programa', choices=PROGRAMA)
    relatorio = forms.FileField(label='relatorio')
    encaminhamento = forms.FileField(label='encaminhamento')


class ParecerOrientadorMestradoForm(forms.Form):
    s1_desempenho = forms.CharField(label='Desempenho', max_length=2048, widget=forms.Textarea)
    s1_projeto = forms.CharField(label='Projeto', max_length=2048)
    s1_outras_atividades = forms.CharField(label='Outras atividades', max_length=5024, widget=forms.Textarea)
    s2_desempenho = forms.CharField(label='Desempenho', max_length=2048, widget=forms.Textarea, required=False)
    s2_metodologia = forms.CharField(label='Metodologia', max_length=2048, widget=forms.Textarea, required=False)
    s2_abordagem = forms.CharField(label='Abordagem', max_length=2048, widget=forms.Textarea, required=False)
    s2_outras_atividades = forms.CharField(label='Outras atividades', max_length=2048, widget=forms.Textarea, required=False)
    s3_resultados = forms.CharField(label='Resultados', max_length=5024, widget=forms.Textarea, required=False)
    s3_perspectivas = forms.CharField(label='Persperctivas', max_length=5024, widget=forms.Textarea, required=False)
    s3_resumo = forms.CharField(label='Resumo', max_length=6048, widget=forms.Textarea, required=False)
    s3_outras_atividades = forms.CharField(label='Outras atividades', max_length=2048, widget=forms.Textarea, required=False)
    report = forms.UUIDField(label='report', widget=forms.HiddenInput)
