# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from aldryn_django.utils import i18n_patterns
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import url, include
from django.views.generic import TemplateView
import aldryn_addons.urls

auth_url_patterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
]


urlpatterns = [
    # add your own patterns here
    path('admin/', admin.site.urls),
    path('auth/', include(auth_url_patterns)),
    path('api/', include('api.urls', namespace='api')),
    
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
