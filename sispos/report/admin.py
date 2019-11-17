from django.contrib import admin
from sispos.report.models import Report, ParecerOrientadorMestrado


class ParecerInline(admin.StackedInline):
    model = ParecerOrientadorMestrado
    extra = 1
    fieldsets = (
        ('primeiro semestre', {
                'classes': ('collapse',),
                'fields': ('s1_desempenho', 's1_projeto', 's1_outras_atividades')
            }
        ),
        ('segundo semestre', {
                'classes': ('collapse',),
                'fields': ('s2_desempenho', 's2_metodologia', 's2_abordagem', 's2_outras_atividades')
            }
        ),
        ('terceiro semestre', {
                'classes': ('collapse',),
                'fields': ('s3_resultados', 's3_perspectivas', 's3_resumo', 's3_outras_atividades')
            }
        )
    )


class ReportModelAdmin(admin.ModelAdmin):
    list_display = ['aluno_name', 'programa', 'orientador', 'relator']
    inlines = [ParecerInline]

    def aluno_name(self, obj):
        return obj.aluno.get_full_name()

    aluno_name.short_description  = 'Aluno'


class ParecerOrientadorMestradoModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Report, ReportModelAdmin)
admin.site.register(ParecerOrientadorMestrado, ParecerOrientadorMestradoModelAdmin)