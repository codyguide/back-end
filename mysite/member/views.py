from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from .models import User
from member.serializers import RegistSerializer, UserSerializer


@api_view(['POST', ])
def regist_view(request):
    if request.method == 'POST':
        serializer = RegistSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = '회원가입되었습니다.'
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)

class UserView(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        id = self.request.user.id
        return User.objects.filter(id=id)


class UserUpdateView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer