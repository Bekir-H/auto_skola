from datetime import datetime

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.models.user import PlatformUser
from api.serializers.user import UserSerializer
from api.utils.error_handler import WrapperException
from api.utils.errors import LOGIN_IS_BLOCKED, ACCOUNT_DISABLED, INVALID_CREDENTIALS, EMAIL_NOT_VERIFIED
from api.serializers.registration import RegisterSerializer
from api.views.auth import AuthenticationView


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(AuthenticationView(data=request.data), idd=serializer.validated_data.get("id"),
                            **serializer.validated_data)

        ime = serializer.validated_data.get("first_name")
        prezime = serializer.validated_data.get("last_name")
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        is_superuser = False
        is_staff = True
        is_active = True
        date_joined = "2021-11-12"
        last_login = "2021-11-12"
        id = 2
        username = serializer.validated_data.get("email")
        is_disabled = False
        is_login_blocked = False

        PlatformUser.objects.raw("INSERT INTO auth_user ('id','password','last_login','is_superuser','username',"
                                 "'first_name','last_name','email','is_staff','is_active','date_joined')"
                                 "VALUES (`id`,`password`,`last_login`,`is_superuser`,`username`,"
                                 "`ime`,`prezime`,`email`,`is_staff`,`is_active`,`date_joined`)")

        PlatformUser.objects.raw("INSERT INTO api_platformuser ('user_ptr_id','is_disabled','is_login_blocked')"
                                 "VALUES (`id`,`is_disabled`,`is_login_blocked`)")

        user = authenticate(AuthenticationView(data=request.data), idd=id,
                            **serializer.validated_data)

        return Response(data=UserSerializer(user).data, status=status.HTTP_200_OK)

