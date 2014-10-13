from __future__ import unicode_literals

try:
    from django.conf.urls import include, url
except ImportError:
    from django.conf.urls.defaults import include, url

from django.contrib import admin
from . import other_admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^other-admin/', include(other_admin.site.urls)),
]
