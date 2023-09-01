from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel

from user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(
        unique=True, blank=True, null=True, verbose_name=_("E-mail")
    )
    password = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name=_("Password"),
    )
    username = models.CharField('Username', max_length=50, unique=True,
                                help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
                                null=True, blank=True)
    coin_token = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Coin Token'))
    code = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_("code")
    )

    is_premium = models.BooleanField(default=False, verbose_name='Premium')
    is_superuser = models.BooleanField(default=False, verbose_name=_("Admin"))
    is_staff = models.BooleanField(default=False, verbose_name=_("Staff"))
    is_active = models.BooleanField(default=False, verbose_name=_("Active"))
    is_verified = models.BooleanField(default=False, verbose_name=_("Verified"))
    is_email_auth = models.BooleanField(default=False, verbose_name=_("Google OAuth"))
    is_google_oauth = models.BooleanField(default=False, verbose_name=_("Google OAuth"))
    google_account_id = models.CharField(
        max_length=150, null=True, blank=True, verbose_name=_("Google account ID")
    )

    USERNAME_FIELD = "username"

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    class Meta:
        db_table = "users__users"
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ("-created_at",)
