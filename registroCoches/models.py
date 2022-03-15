from django.db import models

# Create your models here.

class Marca(models.Model):
	nombreMarca = models.CharField(max_length=30)
	logo = models.ImageField(null=True)
	created=models.DateTimeField(auto_now_add=True, null=True)
	updated=models.DateTimeField(auto_now_add=True, null=True)

	class Meta:
		verbose_name= 'marca'
		verbose_name_plural = 'marcas'

	def __str__(self):
		return self.nombreMarca

class Modelo(models.Model):
	nombreModelo = models.CharField(max_length=30)
	agnoModelo = models.DateField()
	marca =models.ForeignKey (Marca, on_delete=models.CASCADE)
	created=models.DateTimeField(auto_now_add=True, null=True)
	updated=models.DateTimeField(auto_now_add=True, null=True)

	class Meta:
		verbose_name= 'modelo'
		verbose_name_plural = 'modelos'

	def __str__(self):
		return self.nombreModelo


class Coche(models.Model):
	matricula= models.CharField(max_length= 7,primary_key=True)
	fotoCoche = models.ImageField(null=True)
	color =models.CharField(max_length=15)
	kilometros=models.IntegerField(default=0)
	agnoMatriculacion= models.DateField()
	modelo =models.ForeignKey (Modelo, on_delete=models.CASCADE)
	created=models.DateTimeField(auto_now_add=True, null=True)
	updated=models.DateTimeField(auto_now_add=True, null=True)

	class Meta:
		verbose_name= 'coche'
		verbose_name_plural = 'coches'

	def __str__(self):
		return self.matricula