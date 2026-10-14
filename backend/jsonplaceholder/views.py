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
    # GET /api/posts/  ou  /api/posts/?userId=1 - Listar todos os posts ou filtrar por ID de usuário
    def get(self, request):
        try:
            resposta = requests.get(f"{URL}/posts", params=request.query_params, timeout=10)
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


class PostDetalheView(APIView):
    # GET /api/posts/5/ - Obter detalhes de um post específico
    def get(self, request, id_post):
        try:
            resposta = requests.get(f"{URL}/posts/{id_post}", timeout=10)
        except requests.RequestException:
            return erro_conexao()
        return tratar_resposta(resposta)

    # PATCH /api/posts/5/ - Atualizar parcialmente um post específico
    def patch(self, request, id_post):
        try:
            resposta = requests.patch(f"{URL}/posts/{id_post}", json=request.data, timeout=10)
        except requests.RequestException:
            return erro_conexao()
        return tratar_resposta(resposta)

    # DELETE /api/posts/5/ - Excluir um post específico
    def delete(self, request, id_post):
        try:
            resposta = requests.delete(f"{URL}/posts/{id_post}", timeout=10)
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


class UsuarioDetalheView(APIView):
    # GET /api/users/3/ - Obter detalhes de um usuário específico
    def get(self, request, id_usuario):
        try:
            resposta = requests.get(f"{URL}/users/{id_usuario}", timeout=10)
        except requests.RequestException:
            return erro_conexao()
        return tratar_resposta(resposta)