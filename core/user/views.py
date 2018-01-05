from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from .serializers import UsersSerializer


class CustomTokenAuthentication(TokenAuthentication):
    model = Token

    def authenticate_credentials(self, key):
        try:
            token = self.model.objects.select_related('user').get(key=key)
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed('status: APIKeyInvalid')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted')

        return token.user, token


class UsersAPI(ListAPIView):
    authentication_classes = (CustomTokenAuthentication,)

    serializer_class = UsersSerializer

    queryset = User.objects.all()