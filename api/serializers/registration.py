from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    id = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
