import django_filters 
from .models import *

class LibraryFilter(django_filters.FilterSet):
    class Meta:
        model = Library
        fields = '__all__'