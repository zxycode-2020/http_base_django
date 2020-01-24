from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from app01.serializers import UserSerializer,User,ActorSerializer
from app01.models import Student

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = ActorSerializer