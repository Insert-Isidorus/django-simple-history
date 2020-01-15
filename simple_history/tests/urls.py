from __future__ import unicode_literals

from django.contrib import admin
from django.urls import path
from . import other_admin

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('other-admin/', other_admin.site.urls),
]
