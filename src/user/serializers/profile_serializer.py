from rest_framework import serializers

from user.models import User


class ProfileGetSerailizer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    email = serializers.EmailField(read_only=True)
    phone = serializers.CharField(read_only=True)
    full_name = serializers.CharField(read_only=True)
    type = serializers.CharField(read_only=True)
    google_account_id = serializers.CharField(read_only=True)
    is_google_oauth = serializers.BooleanField(read_only=True)
    is_email_auth = serializers.BooleanField(read_only=True)
    default_language = serializers.CharField(read_only=True)


class ProfileUpdateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(max_length=30, required=False)
    full_name = serializers.CharField(max_length=150, required=False)

    class Meta:
        model = User
        fields = ["email", "phone", "full_name"]


class NewPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(max_length=100, required=True)
    confirm_new_password = serializers.CharField(max_length=100, required=True)


class PasswordChangeSerializer(NewPasswordSerializer):
    current_password = serializers.CharField(max_length=100, required=True)