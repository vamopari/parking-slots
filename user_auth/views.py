# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests

from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from oauth2_provider.models import RefreshToken
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from user_auth.utils import generate_oauth_token
from .serializers import UserSerializer, LoginSerializer, UserChangePasswordSerializer


USERNAME_PASSEWORD_MISSING = 'Username and Password are required'

class UserViewSet(CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginViewset(GenericAPIView):
    serializer_class = LoginSerializer
    authentication_classes = [OAuth2Authentication, ]

    def post(self, request, *args, **kwargs):
        data = request.data

        if not (data.get('username') and data.get('password')):
            return Response(USERNAME_PASSEWORD_MISSING, status.HTTP_400_BAD_REQUEST)

        username = data.get('username')
        password = data.get('password')
        token = generate_oauth_token(self.request.get_host(), username, password)

        if token.status_code == 200:
            return Response(token.json(),
                            status=status.HTTP_200_OK)
        return Response(token.text, status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):

    authentication_classes = [OAuth2Authentication, ]

    def post(self, request, *args, **kwargs):
        client_id = settings.CLIENT_ID
        client_secret = settings.CLIENT_SECRET

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'token': request.META['HTTP_AUTHORIZATION'][7:],
                   'token_type_hint': 'access_token',
                   'client_id': client_id,
                   'client_secret': client_secret}

        host = self.request.get_host()
        return Response(
            requests.post(settings.SERVER_PROTOCOLS + host + "/o/revoke_token/", data=payload, headers=headers))


class UserChangePassword(APIView):

    authentication_classes = [OAuth2Authentication, ]

    @swagger_auto_schema(request_body=UserChangePasswordSerializer())
    def post(self, request, *args, **kwargs):

        data = request.data
        user = request.user

        user.set_password(data.get('password'))
        user.save()

        return Response({'msg': 'password changed'}, status=status.HTTP_200_OK)
