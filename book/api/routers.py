from rest_framework import routers
from book.views import AuthorViewSet

router = routers.DefaultRouter()

router.register('author', AuthorViewSet, basename='author')

urlpatterns = router.urls