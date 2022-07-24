from django.utils.translation import pgettext_lazy
from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'created_at')


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def update(self, instance, validated_data):
        updated = False

        valid_fields = ['first_name', 'last_name', 'email']

        for field in valid_fields:
            if field in validated_data:
                updated = True
                setattr(instance, field, validated_data.get(field))

        if updated:
            instance.save()
        if not updated:
            raise serializers.ValidationError({"error": pgettext_lazy(
                "User partial update error", "User not updated at all")})

        return instance


class CreateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        min_length=8, max_length=30, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password')

    def create(self, validated_data):
        
        user = User.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password']
        )
        
        user.save()

        return user
