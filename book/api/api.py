from django.http.response import ResponseHeaders
from rest_framework.response import Response
from book.models import *
from book.api.serializers import  *
from rest_framework.decorators import api_view
from book.views import *
from django.views.generic import ListView
from rest_framework import filters

@api_view(['GET'])
def book_api_view(request):
    
    if request.method == 'GET':
        book = Book.objects.all()
        book_serializer = BookSerializer(book_list_view, many=True)
        return Response(book_serializer.data)
        
    elif request.method == 'POST':
        print(request.data)

@api_view(['GET'])
def library_api_filter(request):

    if request.method == 'GET':
        library = Library.objects.all()
        library_serializer = LibrarySerializer(library_list_view, many=True)
        return Response(library_serializer.data)

