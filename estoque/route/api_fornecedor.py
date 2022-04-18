from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response 
from rest_framework import authentication, permissions

from estoque.serializers import fornecedor_serializer
from estoque.models import Fornecedor
# import estoque.service.fornecedor_service as fornecedor_service 

 
# Create your views here.
class FornecedorList(APIView):
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAdminUser]


	def get(self, request, format=None):
		# request._user = <class 'django.contrib.auth.models.AnonymousUser'>
		# fornecedor = fornecedor_service.listar_fornecedor()
		fornecedor = Fornecedor.objects.all()
		serializer = fornecedor_serializer.FornecedorSerializer(fornecedor, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, format=None):
		serializer = fornecedor_serializer.FornecedorSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			# create_auth_token(instance=serializer.data, created=True)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FornecedorDetalhes(APIView):
	
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAdminUser]

	def get_object(self, pk):
		try:
			return Fornecedor.objects.get(pk=pk)
		except Fornecedor.DoesNotExist:
			raise Http404


	def get(self, request, pk, format=None):
		fornecedor = self.get_object(pk)
		serializer = fornecedor_serializer.FornecedorSerializer(fornecedor)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		fornecedor = self.get_object(pk)
		serializer = fornecedor_serializer.FornecedorSerializer(fornecedor, data=request.data)
		if serializer.is_valid(): # atributo com os dados validados = serializer.validated_data 
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		fornecedor = self.get_object(pk)
		fornecedor.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
