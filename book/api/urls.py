from django.urls import path
from book.views import *


urlpatterns = [
    path('books/', book_list_view),
    path('authors/', author_list_view),
    path('library/', library_list_view, name='library'),
    path('apiviews/', hello_api_view)
]