from django.contrib import admin
from sispos.report.models import Report


class ReportModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Report, ReportModelAdmin)
