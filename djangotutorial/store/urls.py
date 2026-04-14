from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_artigos, name="lista_artigos"),
    path("categoria/<int:categoria_id>/", views.artigos_por_categoria, name="categoria"),
    path("vendedor/<int:vendedor_id>/", views.perfil_vendedor, name="vendedor"),
    path("", views.lista_artigos),
    path("", views.home, name="home"),
    path("", views.home),
]
