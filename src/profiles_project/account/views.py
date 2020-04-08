from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .models import Users
from account.serializers import UsersSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status, exceptions
# from rest_framework.authtoken.views import ObtainAuthToken



# EndPoint To Register a New User 
class UserSignUP(generics.ListCreateAPIView):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()

    def post(self, request, format=None):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# EndPoint To LogIn 
class LogInView(APIView):

        def post(self, request):
            email = request.data['email']
            password = request.data['password']
            if email and password:
                user = authenticate(request, username=request.data["email"], password=request.data["password"])

                if user :
                    token, created = Token.objects.get_or_create(user=user)

                    return Response({'token': token.key})
                else:
                    return Response({'token': "This is credential is not valid"})
            else:
                return Response({'error': "Not Authorized"}, status=401)



