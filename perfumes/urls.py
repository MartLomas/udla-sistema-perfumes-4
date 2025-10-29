from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_perfumes, name='lista_perfumes'),
    path('nuevo/', views.crear_perfume, name='crear_perfume'),
    path('perfumes/<int:pk>/', views.detalle_perfume, name='detalle_perfume'),
    path('eliminar/<int:pk>/', views.eliminar_perfume, name='eliminar_perfume'),
    path('perfumes/<int:pk>/editar/', views.editar_perfume, name='editar_perfume')
]
