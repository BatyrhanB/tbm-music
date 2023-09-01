from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class LoginResponseSerializer(serializers.Serializer):
    code = serializers.CharField(read_only=True, allow_null=False)
    access = serializers.CharField(read_only=True, allow_null=False)


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
