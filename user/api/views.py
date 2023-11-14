from django.contrib.auth import login, authenticate
from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import SignUpSerializer
from rest_framework.response import Response
from user.models import CustomUser



class SignUpAPI(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SignUpSerializer



class LogInAPI(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email, password)

        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


