from django.urls import path 
from . import views

app_name = "tarefas"

urlpatterns = [
    path("", views.tarefas_home, name="home"),
    path("adicionar/", views.tarefas_adicionar, name="adicionar"),

    # CRUD de notícias
    path("noticias/", views.listar_noticias, name="listar_noticias"),
    path("noticias/criar/", views.criar_noticia, name="criar_noticia"),
    path("noticias/<int:id>/", views.noticia_detalhe, name="noticia_detalhe"),
    path("noticias/<int:id>/editar/", views.atualizar_noticia, name="atualizar_noticia"),
    path("noticias/<int:id>/deletar/", views.deletar_noticia, name="deletar_noticia"),
]