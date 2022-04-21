# ~/estoque.serializers.py
from rest_framework import serializers

from estoque.models import Produto



class ProdutoSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Produto 
		fields = [
			'id',
			'nome', 
			'valor_unitario', 
			'codigoIdentificacao',
			'dataFabricacao',
			'dataVencimento',
			'valor_unitario',
			'fornecedor_id',
		]

