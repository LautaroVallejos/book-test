from django.db.models.query import QuerySet
from django.views.generic import ListView
from rest_framework.generics import get_object_or_404

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
class BookViewSet(viewsets.ModelViewSet):
    paginate_by = 100
    model = Book
    context_object_name = 'books'

    serializer_class = BookSerializer
    queryset = Book.objects.all()

    # def get_queryset(self):
    #     qs = super(BookViewSet, self).get_queryset()
    #     qs.order_by('title')
    #     return qs

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
                'title': title,
                'author': author.first_name + ' ' + author.last_name,
                'libraries': libraries.name
            }, status=status.HTTP_201_CREATED)



    def retrieve(self, request, pk = 'title'):
    
        book = get_object_or_404(self.queryset, pk=pk)
        serializer = BookSerializer(book)
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



#==============================
# Library List
class LibraryListView(ListView):
    paginate_by = 10
    model = Library
    context_object_name = 'libraries'


# =================================================================
#Lead endpoint, post method only
class LeadViewSet(viewsets.ModelViewSet):

    serializer_class = LeadSerializer
    
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

book_list_view = BookViewSet.as_view([{'get': 'list'}, {'post': 'create'}])
author_list_view = AuthorViewSet.as_view({'get': 'list'})
library_list_view = LibraryListView.as_view()
lead_list_view = LeadViewSet.as_view({'post': 'post'})
