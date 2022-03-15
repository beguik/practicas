from rest_framework import serializers
from registroCoches.models import Marca, Modelo, Coche


class MarcaSerializer (serializers.ModelSerializer):
	class Meta:
		model = Marca
		fields = '__all__'

class ModeloSerializer (serializers.ModelSerializer):
	class Meta:
		model = Modelo
		fields = '__all__'

class CocheSerializer (serializers.ModelSerializer):
	class Meta:
		model = Coche
		fields = '__all__'