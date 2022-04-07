from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.admin.serializers.update_user import UpdateSerializer
from api.models.user import PlatformUser
from api.serializers.user import UserSerializer
from api.utils.error_handler import WrapperException
from api.utils.errors import NO_PERMISSION


class UpdateUserView(GenericAPIView):
    serializer_class = UpdateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        if not request.user.is_staff:
            raise WrapperException(NO_PERMISSION)
        serializer = UpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        PlatformUser.objects.filter(id=pk).update(
            **serializer.validated_data,
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
