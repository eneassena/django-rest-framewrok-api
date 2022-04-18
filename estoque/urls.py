from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
import estoque.route.api as api

app_label= 'estoque'

urlpatterns = [
	path('produto', api.ProdutoList.as_view()),
	path('produto/<int:pk>', api.ProdutoDetalhes.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
