from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProfileSerializer
from user.models import CustomUser
from rest_framework import generics


class MyProfileAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = CustomUser.objects.get(pk=request.user.id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class ProfileDetailAPI(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'



class ProfileListAPI(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
