from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response 
from rest_framework import authentication, permissions

from estoque.serializers import produto_serializer
import estoque.service.produto_service as produto_service 


# Create your views here.
class ProdutoList(APIView):
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAdminUser]


	def get(self, request, format=None):
		print(request.user)
		print(request.auth)

		# request._user = <class 'django.contrib.auth.models.AnonymousUser'>
		produto = produto_service.listar_produto()
		serializer = produto_serializer.ProdutoSerializer(produto, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, format=None):
		serializer = produto_serializer.ProdutoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			# create_auth_token(instance=serializer.data, created=True)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProdutoDetalhes(APIView):
	def get(self, request, pk, format=None):
		produto = produto_service.get_object(pk)
		serializer = produto_serializer.ProdutoSerializer(produto)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		produto = produto_service.get_object(pk)
		serializer = produto_serializer.ProdutoSerializer(produto, data=request.data)
		if serializer.is_valid():
			# atributo com os dados validados = serializer.validated_data 
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		produto_service.delete_produto(pk)
		return Response(status=status.HTTP_204_NO_CONTENT)
