from django.contrib import admin
from .models.user import Usuario
from .models.bacia_hidrografica import Bacia_Hidrografica
from .models.rio import Rio
from .models.ponto_monitoramento import Ponto_Monitoramento
from .models.casos import Casos
from .models.imagem import Imagem


# Register your models here.
from rbcapp.models import Coleta, Coleta_Substancia, Monitoramento

admin.site.register(Bacia_Hidrografica)
admin.site.register(Rio)
admin.site.register(Usuario)
admin.site.register(Ponto_Monitoramento)
admin.site.register(Casos)
admin.site.register(Monitoramento)
admin.site.register(Coleta)
admin.site.register(Coleta_Substancia)
admin.site.register(Imagem)


