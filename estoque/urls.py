from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
import estoque.route.api_produto as api_produto
from estoque.route import api_funcionario, api_fornecedor, api_estoque



app_label= 'estoque'

urlpatterns = [
	path('produto', api_produto.ProdutoList.as_view()),
	path('produto/<int:pk>', api_produto.ProdutoDetalhes.as_view()),
	
	path('funcionario', api_funcionario.FuncionarioList.as_view()),
	path('funcionario/<int:pk>', api_funcionario.FuncionarioDetalhes.as_view()),
	
	path('fornecedor', api_fornecedor.FornecedorList.as_view()),
	path('fornecedor/<int:pk>', api_fornecedor.FornecedorDetalhes.as_view()),
	
	path('estoque', api_estoque.EstoqueList.as_view()),
	path('estoque/<int:pk>', api_estoque.EstoqueDetalhes.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)
