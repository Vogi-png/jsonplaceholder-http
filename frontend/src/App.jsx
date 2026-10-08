import axios from 'axios';

const http = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
  timeout: 10000,
});

// GET - Listar usuários e posts
export const listarUsuarios = () => http.get('/users/');
export const listarPosts = () => http.get('/posts/');

// GET - Buscar usuário por ID e post por ID de usuário
export const buscarUsuarioPorId = (id_usuario) => http.get(`/users/${id_usuario}/`);
export const buscarPostPorId = (id_usuario) => http.get(`/posts/param?id=${id_usuario}`);

// POST - Criar um novo post
export const criarPost = (postDados) => http.post(`/posts/`, postDados);

// PATCH - Atualizar parcialmente um post
export const atualizarPost = (id_post, titulo) => http.patch(`/posts/${id_post}/`, titulo);

// DELETE - Deletar um post
export const deletarPost = (id_post) => http.delete(`/posts/${id_post}/`);

// Converte qualquer erro do axios numa mensagem (como o except do Python)
export function textoErro(erro) {
  if (erro.response) {
    const msg = erro.response.data?.erro || 'Erro na API';
    return `Status Code: ${erro.response.status} - ${msg}`;
  }
  return 'Não foi possível conectar ao servidor.';
}