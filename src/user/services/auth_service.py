from typing import Tuple, Union

from django.conf import settings
from django.db.models import QuerySet
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

from common.exceptions import *
from common.validators.password_validator import validate_user_password

from user.models import User


class TokenService:
    token = RefreshToken

    @classmethod
    def create_auth_token_by_login_password(
        cls, login: str, password: str
    ) -> Union[Tuple[User, RefreshToken, RefreshToken], None]:
        """create authorization token by user login and password

        Args:
            login (str): _user's email_
            password (str): _user's password_

        Raises:
            ObjectNotFoundException: _return "code" about user not found_

        Returns:
            Union[Tuple[User, RefreshToken, RefreshToken], None]: _return tuple object or None_
        """
        user = authenticate(username=login, password=password)
        if not user:
            raise ObjectNotFoundException(
                {"code": settings.STATUS_CODES.get("user_not_found")}
            )
        token = cls.token.for_user(user)
        return user, token

    @classmethod
    def create_auth_token_by_user(cls, user: QuerySet) -> Union[RefreshToken, None]:
        """create authorization token by user object

        Args:
            user (QuerySet): _user.User object_

        Raises:
            ObjectNotFoundException: _return "code" about user not found_

        Returns:
            Union[RefreshToken, None]: _description_
        """
        if not user:
            raise ObjectNotFoundException(
                {"code": settings.STATUS_CODES.get("user_not_found")}
            )
        token = cls.token.for_user(user)
        return token


class AuthService:
    user_model = User

    @classmethod
    def signup(
        cls, username: str, password: str, confirm_password: str, **kwargs
    ) -> Union[dict, None]:
        """user registering

        Args:
            email (str): _user's email_
            password (str): _user's password_
            confirm_password (str): _confirm password_
            full_name (str): _default None_
            phone (str): _default Noneƒ_

        Raises:
            AlreadyExist: _return code about already existing user_
            SomethingGetWrongException: _return code about unknown server error_

        Returns:
            Union[dict, None]: _return code about user succesfully signed up, and need to verify it or None what means exceptions object_
        """
        user_exist: bool = cls.user_model.objects.filter(username=username).exists()
        if user_exist:
            raise AlreadyExist(
                {"code": settings.STATUS_CODES.get("user_already_exist")}
            )
        verified_password: str = validate_user_password(password, confirm_password)
        try:
            cls.user_model.objects.create_user(
                username=username, password=verified_password, **kwargs
            )
            #cls.send_verification_link(email)
            response: dict = {
                "code": settings.STATUS_CODES.get("user_signed_up"),
            }
            return response
        except:
            raise SomethingGetWrongException(
                {"code": settings.STATUS_CODES.get("unknown")}
            )