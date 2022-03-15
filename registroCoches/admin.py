from django.contrib import admin

from registroCoches.models import Marca, Modelo, Coche

# Register your models here.

class ModeloAdmin(admin.ModelAdmin):
	readonly_fields:('created','updated')
	search_fields=("nombreModelo",)
	list_filter=("marca",)
class MarcaAdmin(admin.ModelAdmin):
	readonly_fields:('created','updated')
	search_fields=("nombreMarca",)
class CocheAdmin(admin.ModelAdmin):
	readonly_fields:('created','updated')
	search_fields=("matricula",)
	list_filter=("modelo",)

admin.site.register(Marca, MarcaAdmin)
admin.site.register(Modelo, ModeloAdmin)
admin.site.register(Coche, CocheAdmin)