from rest_framework import serializers
from member.models import User


class RegistSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def save(self):
        user = User(
            email=self.data['email'],
            username=self.data['username'],
        )
        password = self.data['password']
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"