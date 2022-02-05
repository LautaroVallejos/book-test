"""Dadmin URL Configuration"""

from django.contrib import admin
from django.urls import include, path
from book.api.routers import *
from book.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('book.api.routers')),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh', TokenRefreshView.as_view(), name='token-refresh'),
]
