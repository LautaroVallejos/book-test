from django.db.models.query import QuerySet
from django.views.generic import ListView
from rest_framework.generics import get_object_or_404

import copy

#Local Imports
from .models import *
from book.serializers import *
from .serializers import LeadSerializer, BookSerializer, LibrarySerializer, AuthorSerializer

#Rest Framework Imports
from rest_framework import serializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

#==============================
# BookList

# Do request with curl, postman, etc
# The front can`t render all database
# But the request response correctly
class BookViewSet(viewsets.ModelViewSet):
    paginate_by = 100
    model = Book
    context_object_name = 'books'

    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def list(self, request):
        serializer = BookSerializer(self.queryset, many=True)
        return Response(serializer.data)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()
            title = serializer.validated_data.get('title')
            author = serializer.validated_data.get('author')
            libraries = serializer.validated_data.get('libraries')

            return Response({
                'message': 'The book was created and added succesfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )



    def retrieve(self, request, pk=id):
    
        book = get_object_or_404(self.queryset, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
        

#================================================================
# Book Search Viewset
class BookSearch(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def list(self, request):
        qs = copy.deepcopy(self.queryset)
        qs = qs.filter(title__icontains = request.data.get('title'))
        serializer = BookSerializer(qs)

        return Response(serializer.data)
        


#==============================
# Author View Set        
class AuthorViewSet(viewsets.ModelViewSet):

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    
    paginate_by = 100
    model = Author
    context_object_name = 'authors'

    def list(self, request):
        serializer = AuthorSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request,):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            first_name = serializer.validated_data.get('first_name')
            last_name = serializer.validated_data.get('last_name')

            return Response({
                'message': 'The author was created successfully',
                'first_name': first_name,
                'last_name': last_name
            }, status=status.HTTP_201_CREATED)
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )



#==============================
# Library View Set
class LibraryViewSet(viewsets.ModelViewSet):

    serializer_class = LibrarySerializer
    queryset = Library.objects.all()

    def list(self, request):
        serializer = LibrarySerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            
            name = serializer.validated_data.get('name')

            return Response({
                'message': 'The Library was created succesfully',
                'name': name,
            }, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    paginate_by = 10
    model = Library
    context_object_name = 'libraries'


# =================================================================
#Lead endpoint, post method only
class LeadViewSet(viewsets.ModelViewSet):

    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        model = Lead
        context_object_name = 'lead'

        if serializer.is_valid():
            
            serializer.save()
            email = serializer.validated_data.get('email')
            fullname = serializer.validated_data.get('fullname')
            phone = serializer.validated_data.get('phone')
            library = serializer.validated_data.get('library')
            
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

#=====================================
#Views Exports
#Variable name`s 

book_view_set = BookViewSet.as_view({
    'get': 'list',
    'post': 'create',
    })
author_view_set = AuthorViewSet.as_view({'get': 'list'})
library_view_set = LibraryViewSet.as_view({'get': 'list'})
lead_view_set = LeadViewSet.as_view({'post': 'create'})
