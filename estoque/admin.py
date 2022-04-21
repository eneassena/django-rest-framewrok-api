from django.contrib import admin

from estoque.models import (
	Produto, Fornecedor, Funcionario, Estoque
)


# Register your models here.
admin.site.register(Produto)
admin.site.register(Fornecedor)
admin.site.register(Funcionario)
admin.site.register(Estoque)
