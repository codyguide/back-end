from rest_framework import serializers
from member.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def save(self):
        user = User(
            username=self.data['username'],
            userId=self.data['userId'],
            email=self.data['email'],

        )
        password = self.data['password']
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"