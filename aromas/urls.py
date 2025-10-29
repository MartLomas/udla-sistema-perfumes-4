from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_aromas, name='lista_aromas'),
    path('nuevo/', views.crear_aroma, name='crear_aroma'),
    path('editar/<int:pk>/', views.editar_aroma, name='editar_aroma'),
    path('eliminar/<int:pk>/', views.eliminar_aroma, name='eliminar_aroma'),
]