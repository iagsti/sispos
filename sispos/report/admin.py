from django.contrib import admin
from sispos.report.models import Report


class ReportModelAdmin(admin.ModelAdmin):
    list_display = ['aluno_name', 'programa', 'orientador', 'relator']

    def aluno_name(self, obj):
        return obj.aluno.get_full_name()

    aluno_name.short_description  = 'Aluno'

    
admin.site.register(Report, ReportModelAdmin)