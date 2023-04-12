from random import choices
from .models import ConfirmCode
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserLoginValidateSerializer, UserCreateValidateSerializer, ConfirmCodeValidateSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


@api_view(['POST'])
def authentication_api_view(request):
    serializer = UserLoginValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data)

    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})

    return Response(status=status.HTTP_401_UNAUTHORIZED,
                    data={'error': 'Username or Password wrong!'})


@api_view(['POST'])
def registration_api_view(request):
    serializer = UserCreateValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    code_activate = ''.join(choices('0123456789', k=6))
    user = User.objects.create_user(**serializer.validated_data, is_active=False)

    code = ConfirmCode.objects.create(user_id=user.id, code=code_activate)
    return Response(status=status.HTTP_201_CREATED,
                    data={'user_id': user.id,
                          'code': code.id})


@api_view(["POST"])
def confirm_user_views(request):
    serializer = ConfirmCodeValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        if ConfirmCode.objects.filter(code=request.data['code']):
            User.objects.update(is_active=True)
            return Response(status=status.HTTP_202_ACCEPTED,
                            data={'success': 'confirmed'})

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                        data={'error': 'wrong id or code!'})

    except ValueError:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                        data={'error': 'write code number!'})



