from django.urls import path
from book.views import *


urlpatterns = [
    path('books/', book_list_view),
    path('booksfil/', book_filter_id),
    # path('authors/', author_list_view),
    path('library/', library_list_view, name='lib'),
    path('lead/', lead_list_view),
    path('libfilter/', library_filter)
]
