from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'email')


class UserCreatingSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )

    class Meta:
        model = get_user_model()
        fields = ('email', 'password',  "re_password",)
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def validate(self, attrs):
        if attrs["password"] != attrs["re_password"]:
            raise serializers.ValidationError("Passwords dont match.")
        return attrs

    def create(self, validated_data):
        validated_data.pop("re_password")
        return get_user_model().objects.create_user(**validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('password', None)
        return representation
