from warnings import filters
from django.db.models import fields, query
from django.http.response import JsonResponse
from django.views.generic import ListView
from rest_framework.serializers import Serializer 

#Local Imports
from .models import *
from .api.filters import *
from book.api import serializers
from book.api.serializers import BookSerializer, AuthorSerializer

#Rest Framework Imports
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class BookListView(ListView):
    paginate_by = 100
    model = Book
    context_object_name = 'books'

    def get_queryset(self):
        qs = super(BookListView, self).get_queryset()
        qs.order_by('title')
        return qs


# ==============================
#Book filter by id
class BookFilter(APIView):

    serializer_class = serializers.BookSerializer

    paginate_by = 10
    model = Book
    context_object_name = 'books'

    def get_queryset(self, request):
        qs = super(BookListView, self).get_queryset()
        qs.filter('title')
        
class AuthorListView(ListView):
    paginate_by = 100
    model = Author
    context_object_name = 'authors'


class LibraryListView(ListView):
    paginate_by = 10
    model = Library
    context_object_name = 'libraries'

#============================
class LibraryFilter(ListView):
    model = Library
    context_object_name = 'libraries'

    serializer_class = serializers.LibrarySerializer

    def get(self, request):
        library = Library.objects.all()
        library_serializer = self.serializer_class(fields)
        return Response(library_serializer)


# =================================================================
#Lead endpoint, post method only
class LeadListView(APIView):

    serializer_class = serializers.LeadSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        model = Lead
        context_object_name = 'lead'

        if serializer.is_valid():
            
            serializer.save()
            email = serializer.validated_data.get('email')
            fullname = serializer.validated_data.get('fullname')
            phone = serializer.validated_data.get('phone')
            library = serializer.validated_data.get('library')
            librarySerializer = serializers.Library
            
            return Response({
                'message': "The lead was created succesfully",
                'email': email,
                'fullname': fullname,
                'phone': phone,
                'library': library.name,
            }, status=status.HTTP_201_CREATED)
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

#================================================================
#Probando Viewset
class AuthorViewSet(viewsets.ModelViewSet):

    def list(self, request):
        queryset = Author.objects.all()
        serilizer = AuthorSerializer(queryset, many=True)
        return Response(serilizer.data)



#=====================================
#Views Exports
#Variable name`s 

book_list_view = BookListView.as_view()
book_filter_id = BookFilter.as_view()
author_list_view = AuthorViewSet.as_view({'get': 'list'})
library_list_view = LibraryListView.as_view()
lead_list_view = LeadListView.as_view()
library_filter = LibraryFilter.as_view()
