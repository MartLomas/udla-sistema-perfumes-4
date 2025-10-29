from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_generos, name='lista_generos'),
    path('nuevo/', views.crear_genero, name='crear_genero'),
    path('editar/<int:pk>/', views.editar_genero, name='editar_genero'),
    path('eliminar/<int:pk>/', views.eliminar_genero, name='eliminar_genero'),
]