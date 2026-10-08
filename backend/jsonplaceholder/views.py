import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

URL = "https://jsonplaceholder.typicode.com"


def tratar_resposta(resposta):
    if resposta.ok:
        return Response(resposta.json(), status=resposta.status_code)
    return Response(
        {"erro": f"Erro na API externa. Status code: {resposta.status_code}"},
        status=resposta.status_code,
    )


def erro_conexao():
    return Response(
        {"erro": "Não foi possível conectar à API externa."},
        status=status.HTTP_502_BAD_GATEWAY,
    )


class PostsView(APIView):
      # GET /api/posts/ - Listar todos os posts
      def get(self, request):
         try:
            resposta = requests.get(f"{URL}/posts", timeout=10)
         except requests.RequestException:
            return erro_conexao()
         return tratar_resposta(resposta)

      # GET /api/posts/{id_usuario}/ - Obter posts por ID de usuário
      def get(self, request, id_usuario):
         try:
            resposta = requests.get(f"{URL}/posts/param?id={id_usuario}", timeout=10)
         except requests.RequestException:
            return erro_conexao()
         return tratar_resposta(resposta)

      # POST /api/posts/ - Criar um novo post
      def post(self, request):
         try:
            resposta = requests.post(f"{URL}/posts", json=request.data, timeout=10)
         except requests.RequestException:
            return erro_conexao()
         return tratar_resposta(resposta)

      # DELETE /api/posts/{id_post}/ - Excluir um post
      def delete(self, request, id_post):
         try:
            resposta = requests.delete(f"{URL}/posts/{id_post}", timeout=10)
         except requests.RequestException:
            return erro_conexao()
         return tratar_resposta(resposta)

      # PATCH /api/posts/{id_post}/ - Atualizar parcialmente um post
      def patch(self, request, id_post):
         try:
            resposta = requests.patch(f"{URL}/posts/{id_post}", json=request.data, timeout=10)
         except requests.RequestException:
            return erro_conexao()
         return tratar_resposta(resposta)


class UsuariosView(APIView):
   # GET /api/users/ - Listar todos os usuários
   def get(self, request):
      try:
         resposta = requests.get(f"{URL}/users", timeout=10)
      except requests.RequestException:
         return erro_conexao()
      return tratar_resposta(resposta)

   # GET /api/users/{id_usuario}/ - Obter usuário por ID
   def get(self, request, id_usuario):
      try:
         resposta = requests.get(f"{URL}/users/{id_usuario}", timeout=10)
      except requests.RequestException:
         return erro_conexao()
      return tratar_resposta(resposta)
      