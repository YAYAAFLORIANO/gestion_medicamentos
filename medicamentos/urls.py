from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_medicamentos, name='lista'),
    path('crear/', views.crear_medicamento, name='crear'),
    path('editar/<int:id>/', views.editar_medicamento, name='editar'),
    path('eliminar/<int:id>/', views.eliminar_medicamento, name='eliminar'),
]