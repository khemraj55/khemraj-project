from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import SnippetSerializer, SignUpSerializer
from .models import Snippet
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class SignUpAPI(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=SignUpSerializer

class SnippetViewSet(ModelViewSet):
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
