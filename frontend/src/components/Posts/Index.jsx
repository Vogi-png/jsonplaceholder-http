import { useState } from 'react';
import {
  listarPosts, buscarPostPorId, criarPost, atualizarPost, deletarPost, textoErro,
} from '../../Api.jsx';

export default function Posts() {
  const [resultado, setResultado] = useState(null);
  const [status, setStatus] = useState('');
  

  async function executar(chamada) {
    try {
      const resposta = await chamada();
      setStatus('Status Code: ' + resposta.status);
      setResultado(resposta.data);
    } catch (erro) {
      setStatus(textoErro(erro));
      setResultado(null);
    }
  }

  function buscarPost(){
    const id = prompt('ID do post:');
    if (id) executar(() => buscarPostPorId(id));
  }

  function postsDoUsuario() {
    const id = prompt('ID do usuário:');
    if (id) executar(() => listarPosts(id));
  }

  function criar() {
    const userId = prompt('ID do usuário:');
    const title = prompt('Título:');
    const body = prompt('Conteúdo:');
    if (userId && title && body) {
      executar(() => criarPost({ userId: Number(userId), title, body }));
    }
  }

  async function atualizar() {
    const id = prompt('ID do post:');
    if (!id) return;

    try {
      const respostaBusca = await buscarPostPorId(id);
      const post = respostaBusca.data;

      const confirmado = window.confirm(
        `Tem certeza que quer ATUALIZAR o post?\n\nID: ${post.id}\nTítulo: ${post.title}`
      );
      const title = id && prompt('Novo título:');

      if (confirmado && title && id) {
        executar(() => atualizarPost(id, { title }));
      }
    } catch (erro) {
      setStatus(textoErro(erro));
      setResultado(null);
    }
  }

  async function deletar() {
    const id = prompt('ID do post:');
    if (!id) return;

    try {
      // 1. Busca o post primeiro para obter os detalhes
      const respostaBusca = await buscarPostPorId(id);
      const post = respostaBusca.data;

      const confirmado = window.confirm(
        `Tem certeza que quer DELETAR o post?\n\nID: ${post.id}\nTítulo: ${post.title}`
      );

      if (confirmado) {
        await executar(() => deletarPost(id));
        
      }
    } catch (erro) {
      setStatus(textoErro(erro));
      setResultado(null);
    }
  }

  return (
    <section>
      <h2>Posts</h2>
      <button onClick={() => executar(listarPosts)}>Listar</button>
      <button onClick={buscarPost}>Buscar por ID</button>
      <button onClick={postsDoUsuario}>Posts de um usuário</button>
      <button onClick={criar}>Criar</button>
      <button onClick={atualizar}>Atualizar</button>
      <button onClick={deletar}>Deletar</button>

      {status && <p>{status}</p>}
      {resultado && <pre>{JSON.stringify(resultado, null, 2)}</pre>}
    </section>
  );
}