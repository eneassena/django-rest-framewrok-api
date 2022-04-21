# ~/estoque.serializers.py
from rest_framework import serializers

from estoque.models import Estoque
 

class EstoqueSerializer(serializers.ModelSerializer):
	class Meta:
		model = Estoque 
		fields = [
			'id',
			'produto_id',
			'funcionario_id',
			'dataEstoque',
			'totalEstoque',
			'totalLimit',
			'descricao'
		]
