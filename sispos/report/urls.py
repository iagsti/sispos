from django.urls import path
from sispos.report.views import new, confirmation, report_list, parecer_form, create_parecer_orientador_mestrado

app_name = 'report'

urlpatterns = [
    path('', report_list, name='report_list'),
    path('confirmation/<slug:slug>', confirmation, name='confirmation'),
    path('new', new, name='new'),
    path('<slug:slug>/parecer-orientador-mestrado', parecer_form, name='parecer_orientador_mestrado'),
    path('parecer-orientador-mestrado-create', create_parecer_orientador_mestrado, name='parecer_orientador_mestrado_create')
]
