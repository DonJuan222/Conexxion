from django.contrib import admin
from .models import municipio
from .models import estado
from .models import lugar_Residencia
# from .models import cliente


# Register your models here.

admin.site.register(municipio)
admin.site.register(estado)
admin.site.register(lugar_Residencia)
# admin.site.register(cliente)