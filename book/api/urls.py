from django.urls import path
from book.views import *
from book.api.api import book_api_view
urlpatterns = [
    path('books/', book_list_view)
]