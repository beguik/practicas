from django import forms
from .models import *

class DateTimeInput (forms.DateTimeInput):
	input_type='date'

class MarcaForm(forms.ModelForm):
	class Meta: 
		model= Marca
		fields=['nombreMarca', 
				'logo']
		labels ={
			'nombreMarca':'Nombre',
			'logo': 'Logo'
		}



class ModeloForm(forms.ModelForm):
	class Meta: 
		model= Modelo
		fields=['nombreModelo', 
				'agnoModelo',
				'marca']

		widgets={
			'agnoModelo':DateTimeInput(attrs={'class':'form-control'})
				}

		labels ={
			'nombreModelo':'Nombre',
			'agnoModelo': 'Año',
			'marca': 'Marca'
		}

class CocheForm(forms.ModelForm):
	class Meta:
		model=Coche
		fields=['matricula', 
				'fotoCoche',
				'color',
				'kilometros',
				'agnoMatriculacion',
				'modelo']

		widgets={
			'agnoMatriculacion':DateTimeInput(attrs={'class':'form-control'})
				}


		labels ={
			'matricula':'Matricula',
			'fotoCoche': 'Foto',
			'color': 'Color',
			'kilometros': 'Kilometros',
			'agnoMatriculacion': 'Año de Matriculación',
			'modelo': 'Modelo',
		}

