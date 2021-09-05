from django.urls import path
from book.views import *
from book.api.api import *


urlpatterns = [
    path('book/', book_api_view),
    path('library/', library_api_filter)
]