from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
        self, username, is_superuser, is_staff, is_active, password=None, **kwargs
    ):
        if not username:
            raise ValueError("User must have an username")
        user = self.model(
            username=username,
            is_superuser=is_superuser,
            is_staff=is_staff,
            is_active=is_active,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **kwargs):
        return self._create_user(
            username=username,
            is_superuser=False,
            is_staff=False,
            is_active=False,
            password=password,
            **kwargs
        )

    def create_superuser(self, username, password):
        return self._create_user(
            username=username,
            is_superuser=True,
            is_staff=True,
            is_active=True,
            password=password,
        )