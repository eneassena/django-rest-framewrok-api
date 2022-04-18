from django.http import Http404
from estoque.models import Produto


def get_object(pk):
	try:
		return Produto.objects.get(pk=pk)
	except Produto.DoesNotExist:
		raise Http404

def listar_produto():
	produto = Produto.objects.all()
	return produto

def delete_produto(pk):
	produto = get_object(pk)
	produto.delete()

