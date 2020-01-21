from django.urls import path
from sispos.report.views import new, confirmation, report_list, parecer_form

app_name = 'report'

urlpatterns = [
    path('', report_list, name='report_list'),
    path('confirmation/<slug:slug>', confirmation, name='confirmation'),
    path('new', new, name='new'),
    path('parecer-orientador-mestrado', parecer_form, name='parecer_orientador_mestrado'),
]
