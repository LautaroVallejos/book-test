from rest_framework import routers
from book.views import AuthorViewSet, BookViewSet, LibraryViewSet, LeadViewSet

router = routers.DefaultRouter()

router.register('author', AuthorViewSet, basename='author')
router.register('book', BookViewSet, basename='book')
router.register('library', LibraryViewSet, basename='library')
router.register('lead', LeadViewSet, basename='lead')

urlpatterns = router.urls