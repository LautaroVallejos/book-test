from rest_framework import routers
from book.views import AuthorViewSet, BookViewSet

router = routers.DefaultRouter()

router.register('author', AuthorViewSet, basename='author')
router.register('book', BookViewSet, basename='book')

urlpatterns = router.urls