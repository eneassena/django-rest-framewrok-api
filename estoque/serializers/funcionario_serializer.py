# ~/estoque.serializers.py
from rest_framework import serializers

from estoque.models import Funcionario


class FuncionarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Funcionario 
		fields = [ 
			'nome',
			'perfilFuncionario',
			'email',
			'telefone'
		]
