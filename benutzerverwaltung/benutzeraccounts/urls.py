from django.conf.urls import url
from django.conf.urls import include
from django.contrib.auth.views import (login, logout)
from django.core.urlresolvers import reverse
from . import views

#alle URLs die aufrubar sind, werden hier aufgelistet. Die Views-Funktionen werden hiermit aufgerufen

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'benutzeraccounts/login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
]
