from django.urls import path
from sispos.report.views import new, confirmation

app_name = 'report'

urlpatterns = [
    path('new', new, name='new'),
    path('confirmation/<slug:slug>', confirmation, name='confirmation')
]

