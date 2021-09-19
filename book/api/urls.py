from django.urls import path
from book.views import *

urlpatterns = [
    path('books/', book_view_set),
    path('authors/', author_view_set),
    path('library/', library_view_set),
    path('lead/', lead_view_set),
]
