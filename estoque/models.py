from django.db import models

# Create your models here.



class Fornecedor(models.Model):
	nomeContato=models.CharField(max_length=150)
	empresa=models.CharField(max_length=255)
	email=models.CharField(max_length=200)
	telefoneFixo=models.CharField(max_length=15)

	def __str__(self):
		return self.nomeContato

class Funcionario(models.Model):
	nome=models.CharField(max_length=150)
	perfilFuncionario=models.CharField(max_length=100)
	email=models.CharField(max_length=200)
	telefone=models.CharField(max_length=15)

	def __str__(self):
		return self.nome


class Produto(models.Model):
	nome = models.CharField(max_length=150)
	codigoIdentificacao = models.CharField(max_length=20)
	dataFabricacao = models.CharField(max_length=20)
	dataVencimento = models.CharField(max_length=20)
	valor_unitario = models.FloatField()
	fornecedor_id = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome


class Estoque(models.Model):
	produto_id=models.ForeignKey(Produto, on_delete=models.CASCADE)
	funcionario_id=models.ForeignKey(Funcionario, on_delete=models.CASCADE)
	dataEstoque=models.DateField()
	totalEstoque=models.IntegerField()
	totalLimit=models.IntegerField()
	descricao= models.TextField()

	def __str__(self):
		return self.produto_id






 



