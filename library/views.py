from rest_framework import viewsets
from .models import Genre, Author, Book, Member, BorrowingHistory
from .serializers import GenreSerializer, AuthorSerializer, BookSerializer, MemberSerializer, BorrowingHistorySerializer
from .permissions import IsMember, IsSuperAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken  
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken

class CustomPagination(PageNumberPagination):
    page_size = 5

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsSuperAdmin()]
        return [IsSuperAdmin()]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsSuperAdmin()]
        return [IsSuperAdmin()]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [IsMember()] 
        elif self.action in ['create', 'update', 'destroy']:
            return [IsSuperAdmin()]  
        return [IsAuthenticated()]

    search_fields = ['title', 'authors__first_name', 'authors__last_name', 'genre__name']
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['title', 'published_date']

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsSuperAdmin()]
        return [IsSuperAdmin()]

class BorrowingHistoryViewSet(viewsets.ModelViewSet):
    queryset = BorrowingHistory.objects.all()
    serializer_class = BorrowingHistorySerializer

    def get_permissions(self):
        if self.action == 'list':
            return [IsSuperAdmin()]
        elif self.action in ['create', 'update', 'destroy']:
            return [IsSuperAdmin()]
        return super().get_permissions()

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['member__user__username', 'due_date']
    search_fields = ['book__title']

class MemberRegistrationView(generics.CreateAPIView):
    serializer_class = MemberSerializer

    def perform_create(self, serializer):
        serializer.save()

class ObtainAuthToken(TokenObtainPairView):
    permission_classes = []  

class TokenRefreshView(TokenRefreshView):
    permission_classes = []  

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            if not refresh_token:
                return Response({"error": "No refresh token provided"}, status=400)
            
            try:
                token = RefreshToken(refresh_token)
                token.blacklist() 

                return Response({"message": "Successfully logged out"}, status=200)
            except InvalidToken:
                return Response({"error": "Invalid token"}, status=400)

        except Exception as e:
            return Response({"error": "Failed to logout", "detail": str(e)}, status=400)
