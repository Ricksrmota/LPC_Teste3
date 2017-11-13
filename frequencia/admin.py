from django.contrib import admin
from frequencia.models import Funcionario
from frequencia.models import Ponto
from frequencia.models import Configuracao

# Register your models here.
admin.site.register(Funcionario)
admin.site.register(Ponto)
admin.site.register(Configuracao)
