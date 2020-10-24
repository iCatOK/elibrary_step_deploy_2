from django.shortcuts import render
from rest_framework import serializers, generics
from .serializers import UserSerializer
from .models import User
from .permissions import IsLibrarianOrNothing

# Create your views here.

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [
        IsLibrarianOrNothing,
    ]

class UserDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [
        IsLibrarianOrNothing
    ]
