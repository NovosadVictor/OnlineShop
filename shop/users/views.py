from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_protect


class UserView(APIView):

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UsersView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class LoginView(APIView):

    @csrf_protect
    def post(self, request):
        username = request.data['username']
        print(username)
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response("there is no such users")


class LogoutView(APIView):

    def get(self, request):
        logout(request)
        return Response("cool")


class RegistrationView(APIView):

    def post(self, request):
        if request.data['password1'] != request.data['password2']:
            return Response("passwords dosnt equal")
        username = request.data['username']
        password = request.data['password2']
        email = request.data['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)


# Create your views here.
