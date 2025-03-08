"""
URL configuration for library_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from library.views import MemberRegistrationView, LogoutView
from library.views import ObtainAuthToken
def home(request):
    return HttpResponse("Welcome to the Library Management System!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('library.urls')),
    path('', home, name='home'), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    
    path('register/', MemberRegistrationView.as_view(), name='member-register'),
    path('login/', ObtainAuthToken.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
