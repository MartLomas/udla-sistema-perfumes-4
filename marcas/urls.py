from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_marcas, name='lista_marcas'),
    path('nuevo/', views.crear_marca, name='crear_marca'),
    path('editar/<int:pk>/', views.editar_marca, name='editar_marca'),
    path('eliminar/<int:pk>/', views.eliminar_marca, name='eliminar_marca'),
]