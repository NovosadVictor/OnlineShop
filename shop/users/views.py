from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .serializers import UserSerializer


class LoginView(APIView):

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
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
        user = User.objects.create(username=username, password=password, email=email)
        serializer = UserSerializer(user)
        return Response(serializer.data)


# Create your views here.
