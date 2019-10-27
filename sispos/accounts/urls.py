from django.urls import path
from sispos.accounts.views import login, authorize, user, logout_view

app_name = 'accounts'

urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout_view, name='logout'),
    path('authorize', authorize, name='authorize'),
    path('user', user, name='user')
]
