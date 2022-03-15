from django.shortcuts import render,redirect, HttpResponse
from registroCoches.models import *
from registroCoches.forms import *
from django.views.generic import TemplateView





# Create your views here.

def home(request):
	return render(request, "registroCoches/home.html")

def marca(request):
	modelos=Modelo.objects.all()
	marcas=Marca.objects.all().extra(select={'minusculas':'lower(nombreMarca)'}).order_by("minusculas")
	return render(request, "registroCoches/marca.html",{"marcas":marcas, "modelos":modelos} )


def crearMarca(request):
	if request.method=='POST':
		form=MarcaForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('Marca')
	else:
		form=MarcaForm()
	return render (request,"registroCoches/crearMarca.html", {"form":form,} )


def editarMarca(request,id):
	marca=Marca.objects.get(id=id)
	if request.method=="GET":
		form=MarcaForm(instance = marca)
	else:
		form =MarcaForm (request.POST, instance=marca)
		if form.is_valid():
			form.save()
		return redirect('Marca')
	return render (request,"registroCoches/editarMarca.html", {"form":form,"marca":marca,} )


def eliminarMarca (request,id):
	marca=Marca.objects.get(id=id)
	if request.method=="POST":
		marca.delete()
		return redirect('Marca')
	return render (request,"registroCoches/eliminarMarca.html", {"marca":marca,} )


def marcamodelos(request, id):
	marcas=Marca.objects.get(id=id)
	modelos=Modelo.objects.filter(marca=marcas)
	return render(request, "registroCoches/marcamodelos.html",{"marcas":marcas, "modelos":modelos} )

def crearModelo(request):

	if request.method=='POST':
		form=ModeloForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('Marca')
	else:
		form=ModeloForm()
	return render (request,"registroCoches/crearModelo.html", {"form":form,} )

def editarModelo(request,id):
	modelo=Modelo.objects.get(id=id)
	if request.method=="GET":
		form=ModeloForm(instance = modelo)
	else:
		form =ModeloForm (request.POST, instance=modelo)
		if form.is_valid():
			form.save()
		return redirect('Marca')
	return render (request,"registroCoches/editarModelo.html", {"form":form, "modelo":modelo} )

def eliminarModelo (request,id):
	modelo=Modelo.objects.get(id=id)
	if request.method=="POST":
		modelo.delete()
		return redirect('Marca')
	return render (request,"registroCoches/eliminarModelo.html", {"modelo":modelo,} )

def coche (request):
	marcas=Marca.objects.all()
	modelos=Modelo.objects.all()
	coches=Coche.objects.all()
	contador=Coche.objects.count()
	diccionarios= Coche.objects.select_related('modelo').values_list('modelo__marca','matricula')
	dicc={}
	for k, v in diccionarios:
		dicc.setdefault(k, []).append(v)
	
	return render(request, "registroCoches/coche.html",{"marcas":marcas, "modelos":modelos, "coches":coches, "contador":contador, "diccionarios":diccionarios,"dicc":dicc,})

def crearCoche(request):

	if request.method=='POST':
		form=CocheForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('Coche')
	else:
		form=CocheForm()
	return render (request,"registroCoches/crearCoche.html", {"form":form,} )	
	
def buscarMatricula(request):

		mat= request.POST['matricula']
		try:
			coche=Coche.objects.get(matricula=mat)
		except Coche.DoesNotExist:
			coche="Ese identificador no corresponde a ningún vehículo"	

		return render(request, "registroCoches/buscarMatricula.html",{"coche":coche})

def buscarFecha(request):

	if request.POST['fecha']:
		fecha=request.POST['fecha']
		coches=Coche.objects.filter(agnoMatriculacion__lte= fecha).order_by("-agnoMatriculacion")
		return render(request, "registroCoches/buscarFecha.html",{"fecha":fecha, "coches":coches})
	else:
		mensaje="Debe introducir un registro adecuado"
		return render(request, "registroCoches/buscarFecha.html",{"mensaje":mensaje})

def cocheMarca(request,id):
	marcas=Marca.objects.all()
	modelos=Modelo.objects.all()
	coches=Coche.objects.all()
	diccionarios= Coche.objects.select_related('modelo').values_list('modelo__marca','matricula')
	dicc={}
	for k, v in diccionarios:
		dicc.setdefault(k, []).append(v)

	control=dicc[id]
	identificador=id
	
	return render(request, "registroCoches/cocheMarca.html",{"marcas":marcas, "modelos":modelos, "coches":coches,"diccionarios":diccionarios,"dicc":dicc,"control":control,"identificador":identificador,})

def editarCoche(request,id):
	coche=Coche.objects.get(matricula=id)
	if request.method=="GET":
		form=CocheForm(instance = coche)
	else:
		form =CocheForm (request.POST, instance=coche)
		if form.is_valid():
			form.save()
		return redirect('Coche')
	return render (request,"registroCoches/editarCoche.html", {"form":form, "coche":coche} )

def eliminarCoche (request,id):
	coche=Coche.objects.get(matricula=id)
	if request.method=="POST":
		coche.delete()
		return redirect('Coche')
	return render (request,"registroCoches/eliminarCoche.html", {"coche":coche,} )