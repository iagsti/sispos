from django.urls import path
from sispos.core.views import index

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
]
