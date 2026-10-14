from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UsuariosView.as_view()),
    path('users/<int:id_usuario>/', views.UsuarioDetalheView.as_view()),
    path('posts/', views.PostsView.as_view()),
    path('posts/<int:id_post>/', views.PostDetalheView.as_view()),
]