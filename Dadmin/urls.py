"""Dadmin URL Configuration"""

from django.contrib import admin
from django.urls import include, path
from book.api.urls import *
from book.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('book.api.urls'))
]
