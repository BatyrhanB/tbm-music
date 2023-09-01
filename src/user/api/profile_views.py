from django.http import HttpRequest
from django.conf import settings

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from user.serializers.profile_serializer import (
    PasswordChangeSerializer,
    ProfileGetSerailizer,
    ProfileUpdateSerializer,
)
from user.services.auth_service import TokenService
from user.services.profile_service import ProfileService


class ProfileAPIView(GenericAPIView):
    serializer_class = ProfileUpdateSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get(self, request: HttpRequest, *args, **kwargs) -> Response:
        data = ProfileGetSerailizer(request.user).data
        return Response(
            data={
                "data": data,
                "code": settings.STATUS_CODES.get("user_get_profile"),
            }
        )

    def patch(self, request: HttpRequest, *args, **kwargs) -> Response:
        serializer = self.serializer_class(
            request.user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = ProfileGetSerailizer(request.user).data
        return Response(
            data={
                "data": data,
                "code": settings.STATUS_CODES.get("user_patch_profile"),
            }
        )


class PasswordChangeAPIView(GenericAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request: HttpRequest, *args, **kwargs) -> Response:
        response = Response()

        seirializer = self.serializer_class(data=request.data)
        seirializer.is_valid(raise_exception=True)
        user = ProfileService.change_passowrd(
            user=request.user,
            current_password=seirializer.validated_data.get("current_password"),
            new_password=seirializer.validated_data.get("new_password"),
            confirm_new_password=seirializer.validated_data.get("confirm_new_password"),
        )
        token = TokenService.create_auth_token_by_user(user)
        response.data = {
            "code": settings.STATUS_CODES.get("password_successfulyl_changed"),
        }
        return response
