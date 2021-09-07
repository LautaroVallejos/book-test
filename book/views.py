from django.db.models import fields, query
from django.views.generic import ListView

from .models import *

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .api.filters import *

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

class LibraryFilter(APIView):
    model = Library
    context_object_name = 'libraries'

    serializer_class = serializers.LibrarySerializer

    def get(self, request, format=None):
        library = Library.objects.all()
        library_serializer = self.serializer_class(fields)
        return Response({library_serializer})

# =================================================================
#Lead endpoint, post method
class LeadListView(APIView):

    serializer_class = serializers.LeadSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        model = Lead
        context_object_name = 'leads'

        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            fullname = serializer.validated_data.get('fullname')
            phone = serializer.validated_data.get('phone')
            library = serializer.validated_data.get('library')
            
            return Response({
                'email': email,
                'fullname': fullname,
                'phone': phone,
                'library': library,
            })
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    # def get_queryset(self):
    #     qs = super(LeadListView, self).get_queryset()
    #     qs.order_by('phone')
    #     return qs


#Ejemplo practico de una api view
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
lead_list_view = LeadListView.as_view()
library_filter = LibraryFilter.as_view()