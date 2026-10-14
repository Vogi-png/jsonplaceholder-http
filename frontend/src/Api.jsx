import axios from 'axios';

const http = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
  timeout: 10000,
});

// GET - Listar usuários e posts
export const listarUsuarios = () => http.get('/users/');

// GET - Listar TODOS os posts ou com opção de filtrar por ID de usuário
export const listarPosts = (userId) => http.get('/posts/', { params: userId ? { userId } : {} });

// GET - Buscar post por ID
export const buscarPostPorId = (id) => http.get(`/posts/${id}/`);

// GET - Buscar usuário por ID e post por ID de usuário
export const buscarUsuarioPorId = (id) => http.get(`/users/${id}/`);

// POST - Criar um novo post
export const criarPost = (postDados) => http.post(`/posts/`, postDados);

// PATCH - Atualizar parcialmente um post
export const atualizarPost = (id, dados) => http.patch(`/posts/${id}/`, dados);

// DELETE - Deletar um post
export const deletarPost = (id) => http.delete(`/posts/${id}/`);

// Converte qualquer erro do axios numa mensagem (como o except do Python)
export function textoErro(erro) {
  if (erro.response) {
    const msg = erro.response.data?.erro || 'Erro na API';
    return `Status Code: ${erro.response.status} - ${msg}`;
  }
  return 'Não foi possível conectar ao servidor.';
}