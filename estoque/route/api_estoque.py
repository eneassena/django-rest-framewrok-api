from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.authtoken.models import Token 
from rest_framework import authentication, permissions

from estoque.models import Estoque
from estoque.serializers import estoque_serializer
# import estoque.service.produto_service as produto_service 

 
# Create your views here.
class EstoqueList(APIView):
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAdminUser]


	def get(self, request, format=None):  
		# request._user = <class 'django.contrib.auth.models.AnonymousUser'>
		# estoque = produto_service.listar_produto()
		estoque = Estoque.objects.all()
		serializer = estoque_serializer.EstoqueSerializer(estoque, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, format=None):
		serializer = estoque_serializer.EstoqueSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			# create_auth_token(instance=serializer.data, created=True)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EstoqueDetalhes(APIView):

	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAdminUser]

	
	def get_object(self, pk):
		try:
			return Estoque.objects.get(pk=pk)
		except Estoque.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		# estoque = produto_service.get_object(pk)
		estoque = self.get_object(pk)
		serializer = estoque_serializer.EstoqueSerializer(estoque)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		estoque = self.get_object(pk)
		serializer = estoque_serializer.EstoqueSerializer(estoque, data=request.data)
		if serializer.is_valid():
			# atributo com os dados validados = serializer.validated_data 
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		estoque = Estoque.objects.get(pk=pk)
		estoque.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
