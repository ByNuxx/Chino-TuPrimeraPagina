from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear/', views.crear_pokemon, name='crear_pokemon'),
    path('listar/', views.listar_pokemon, name='lista_pokemon'),
    path('eliminar/<int:pokemon_id>/', views.eliminar_pokemon, name='eliminar_pokemon'),
]