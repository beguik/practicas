from django.urls import path
from registroCoches import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', views.home, name="Inicio"),
    path('marca', views.marca, name="Marca"),
    path('crearMarca', views.crearMarca, name="crearMarca"),
    path('editarMarca/<int:id>', views.editarMarca, name="editarMarca"),
    path('eliminarMarca/<int:id>', views.eliminarMarca, name="eliminarMarca"),
    path('marcamodelos/<int:id>/', views.marcamodelos, name="marcamodelos"),
    path('crearModelo', views.crearModelo, name="crearModelo"),
    path('editarModelo/<int:id>', views.editarModelo, name="editarModelo"),
    path('eliminarModelo/<int:id>', views.eliminarModelo, name="eliminarModelo"),
    path('coche', views.coche, name="Coche"),
    path('crearCoche', views.crearCoche, name="crearCoche"),
    path('buscarMatricula', views.buscarMatricula, name="buscarMatricula"),
    path('buscarFecha', views.buscarFecha, name="buscarFecha"),
    path('cocheMarca/<int:id>', views.cocheMarca, name="cocheMarca"),
    path('editarCoche/<str:id>', views.editarCoche, name="editarCoche"),
    path('eliminarCoche/<str:id>', views.eliminarCoche, name="eliminarCoche"),
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

