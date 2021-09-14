from django.db.models.query import QuerySet
from django.views.generic import ListView

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
class BookListView(ListView):
    paginate_by = 100
    model = Book
    context_object_name = 'books'

    def get_queryset(self):
        qs = super(BookListView, self).get_queryset()
        qs.order_by('title')
        return qs

#==============================
# Author View Set        
class AuthorViewSet(viewsets.ModelViewSet):

    serializer_class = AuthorSerializer

    def list(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)

        return Response(serializer.data)

    # paginate_by = 100
    # model = Author
    # context_object_name = 'authors'


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

book_list_view = BookListView.as_view()
author_list_view = AuthorViewSet.as_view({'get': 'list'})
library_list_view = LibraryListView.as_view()
lead_list_view = LeadViewSet.as_view({'post': 'post'})
