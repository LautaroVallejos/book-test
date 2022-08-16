from rest_framework.generics import get_object_or_404
#Local Imports
from .models import *
# from book.models import User
from book.serializers import *
from .serializers import LeadSerializer, BookSerializer, LibrarySerializer, AuthorSerializer, UserSerializer

#Rest Framework Imports
import json
from collections import OrderedDict
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

#==============================
# BookViewSet

# The books views return from a diferent way in this case, they are parsed to json before return it.
# Else the page not response for the heavy quantity of objects and crash.

# You can filter by 'book/[id]' or by 'book/?search=[input text]'
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def list(self, request):
        serializer = BookSerializer(self.queryset, many=True)
        titleList = serializer.data
        # parse all objects to json and return it
        response = json.dumps(titleList)

        return Response(response)

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
        

#==============================
# Author View Set        
class AuthorViewSet(viewsets.ModelViewSet):

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def list(self, request):
        serializer = AuthorSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
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

    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

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
