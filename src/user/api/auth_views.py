from django.http import HttpRequest
from django.conf import settings

from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from user.serializers.auth_serializer import LoginSerializer, LoginResponseSerializer, SignUpSerializer
from user.services.auth_service import AuthService, TokenService


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    response_serializer_class = LoginResponseSerializer
    permission_classes = (AllowAny,)

    def post(self, request: HttpRequest, *args, **kwargs) -> Response:
        response = Response()
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        user, token = TokenService.create_auth_token_by_login_password(
            login=serializer.validated_data.get("username"),
            password=serializer.validated_data.get("password"),
        )
        response_data = {"code": settings.STATUS_CODES.get("user_signed_in"), "access": f"{token.access_token}"}
        response_serializer = self.response_serializer_class(data=response_data)
        response_serializer.is_valid()
        response.data = response_data
        return response


class SignUpAPIView(GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = (AllowAny,)

    def post(self, request: HttpRequest, *args, **kwargs):
        serilizer = self.serializer_class(data=request.data)
        serilizer.is_valid(raise_exception=True)
        response = AuthService.signup(
            username=serilizer.validated_data.get("username"),
            password=serilizer.validated_data.get("password"),
            confirm_password=serilizer.validated_data.get("confirm_password"),
        )
        return Response(data=response, status=201)


class LogOutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: HttpRequest, *args, **kwargs) -> Response:
        response = Response()
        response.data = {"code": settings.STATUS_CODES.get("user_log_out")}
        return response
