from django.views.generic import ListView

from .models import Book, Author, Library

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from book.api import serializers
class BookListView(ListView):
    paginate_by = 100
    model = Book
    context_object_name = 'books'

    def get_queryset(self):
        qs = super(BookListView, self).get_queryset()
        qs.order_by('title')
        return qs


class AuthorListView(ListView):
    paginate_by = 100
    model = Author
    context_object_name = 'authors'


class LibraryListView(ListView):
    paginate_by = 10
    model = Library
    context_object_name = 'libraries'


class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Retorna la lista de caracteristicas del api view"""
        an_apiview = ['lorem ipstun', 
        'lorem ipsum dolor sit amet, consectetur', 
        'jajaxd', 
        'estos son apiviews', 
        'se mapean manualmente'
        ]

        return Response({'message': 'hello littel bitch', 'an_apiview': an_apiview})

    def post(self, request):
        """Crea mensaje"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

hello_api_view = HelloApiView.as_view()
book_list_view = BookListView.as_view()
author_list_view = AuthorListView.as_view()
library_list_view = LibraryListView.as_view()
