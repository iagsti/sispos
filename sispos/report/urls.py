from django.urls import path
from sispos.report.views import new, confirmation, report_list

app_name = 'report'

urlpatterns = [
    path('new', new, name='new'),
    path('confirmation/<slug:slug>', confirmation, name='confirmation'),
    path('', report_list, name='report_list')
]
