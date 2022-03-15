from rest_framework import generics
from rest_framework.response import Response
from registroCoches.models import Marca, Modelo, Coche
from registroCoches.serializer import MarcaSerializer, ModeloSerializer, CocheSerializer


class MarcaApi (generics.ListCreateAPIView):
	queryset = Marca.objects.all()
	serializer_class = MarcaSerializer

class MarcaUpdateApi (generics.RetrieveUpdateAPIView):
	queryset=Marca.objects.all()
	serializer_class=MarcaSerializer

class MarcaDeleteApi (generics.DestroyAPIView):
	queryset=Marca.objects.all()
	serializer_class=MarcaSerializer

class ModeloApi (generics.ListCreateAPIView):
	queryset = Modelo.objects.all()
	serializer_class = ModeloSerializer

class ModeloUpdateApi (generics.RetrieveUpdateAPIView):
	queryset=Modelo.objects.all()
	serializer_class=ModeloSerializer

class ModeloDeleteApi (generics.DestroyAPIView):
	queryset=Modelo.objects.all()
	serializer_class=ModeloSerializer

class CocheApi (generics.ListCreateAPIView):
	queryset = Coche.objects.all()
	serializer_class = CocheSerializer

class CocheUpdateApi (generics.RetrieveUpdateAPIView):
	queryset=Coche.objects.all()
	serializer_class=CocheSerializer

class CocheDeleteApi (generics.DestroyAPIView):
	queryset=Coche.objects.all()
	serializer_class=CocheSerializer
