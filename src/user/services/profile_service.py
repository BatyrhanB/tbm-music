import random
from django.conf import settings


from typing import Union

from common.exceptions import *
from common.validators.password_validator import validate_user_password

from user.models import User


class ProfileService:
    user_model = User

    @classmethod
    def get_user_by_email(cls, email: str) -> Union[None, User]:
        user = cls.user_model.objects.filter(email=email).first()
        if not user:
            raise ObjectNotFoundException(
                {"code": settings.STATUS_CODES.get("user_not_found")}
            )
        return user

    @classmethod
    def get_user(cls, **filter) -> Union[None, User]:
        user = cls.user_model.objects.filter(**filter).first()
        if not user:
            raise ObjectNotFoundException(
                {"code": settings.STATUS_CODES.get("user_not_found")}
            )
        return user

    @staticmethod
    def generate_code():
        digit = str(random.randint(1, 999_999))
        code = digit if len(digit) == 6 else "0" * (6 - len(digit)) + digit
        return code

    @classmethod
    def change_passowrd(
        cls,
        user: User,
        current_password: str,
        new_password: str,
        confirm_new_password: str,
    ) -> Union[None, User]:
        """_Change password_

        Args:
            user (User): _user's object_
            current_password (str): _user's old password_
            new_password (str): _new password_
            confirm_new_password (str): _new password_

        Raises:
            IncorrectPasswordException: _Exceptions about current password doenst match_

        Returns:
            Union[None, User]: _return user's object or exception_
        """
        if not user.check_password(raw_password=current_password):
            raise IncorrectPasswordException(
                {"code": settings.STATUS_CODES.get("password_not_correct")}
            )
        cls.change_password_force(user, new_password, confirm_new_password)

        return user

    @classmethod
    def verify_user_and_change_passowrd(
        cls,
        code: str,
        email: str,
        new_password: str,
        confirm_new_password: str,
    ) -> User:
        user = cls.get_user(email=email, code=code)
        user = cls.change_password_force(user, new_password, confirm_new_password)
        return user

    @classmethod
    def change_password_force(
        cls, user: User, new_password: str, confirm_new_password: str
    ) -> Union[None, User]:
        correct_new_password = validate_user_password(
            password=new_password, conf_password=confirm_new_password
        )
        user.set_password(correct_new_password)
        user.save()
        return user
