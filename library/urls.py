from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenreViewSet, AuthorViewSet, BookViewSet, MemberViewSet, BorrowingHistoryViewSet, MemberRegistrationView

router = DefaultRouter()

# Register all your viewsets to the same router
router.register(r'genres', GenreViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'members', MemberViewSet)
router.register(r'borrowing-history', BorrowingHistoryViewSet)

   


urlpatterns = [
    path('', include(router.urls)),  # API views will be available directly under the /api/ prefix

]
