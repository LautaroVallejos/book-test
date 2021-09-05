from django.http.response import ResponseHeaders
from rest_framework.response import Response
from book.models import *
from book.api.serializers import  *
from rest_framework.decorators import api_view
from book.views import book_list_view
from django.views.generic import ListView

@api_view(['GET'])
def book_api_view(request):
    
    if request.method == 'GET':
        return print(book_list_view)
