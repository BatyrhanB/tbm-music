import coreapi
from rest_framework.schemas.coreapi import AutoSchema
import coreschema


class PasswordResetSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == "POST":
            api_fields = [
                coreapi.Field(
                    name="email",
                    required=True,
                    location="form",
                    schema=coreschema.String(description="user's email"),
                ),
                coreapi.Field(
                    name="code",
                    required=True,
                    location="form",
                    schema=coreschema.String(description="verification"),
                ),
                coreapi.Field(
                    name="new_password",
                    required=True,
                    location="form",
                    schema=coreschema.String(description="new password"),
                ),
                coreapi.Field(
                    name="confirm_new_password",
                    required=True,
                    location="form",
                    schema=coreschema.String(description="confirm new password"),
                ),
            ]
        return self._manual_fields + api_fields
