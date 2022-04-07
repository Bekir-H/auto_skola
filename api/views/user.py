from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers.user import UserSerializer


class UserView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(data=UserSerializer(request.user).data, status=status.HTTP_200_OK)
