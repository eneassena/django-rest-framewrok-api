# anavitoria,12345678#E

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions, authentication

from django.contrib.auth.models import User 
from estoque.serializers import user_serializer
# UserAuthTokenSerializer

class UserCreate(APIView):
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAdminUser]

	def _get_object(self):
		return User.objects.all()

	def get(self, request, format=None):
		users = self._get_object()
		serializer = user_serializer.UserAuthTokenSerializer(users, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


	def post(self, request, format=None):

		serializer = user_serializer.UserAuthTokenSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetelhas(APIView):
	def _get_object(self, pk):
		return User.objects.get(pk=pk)

	def get(self, request, pk, format=None):
		user = self._get_object(pk)
		serializer = user_serializer.UserAuthTokenSerializer(user)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, pk, format=None):
		user = self._get_object(pk)

		serializer = user_serializer.UserAuthTokenSerializer(user, data=request.data)
		if serializer.is_valid(): 
			senha = serializer.validated_data['password']
			user.senha = user.set_password(senha)
			user.save()
			# serializer.save()
			return Response(serializer.data)
		return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)





