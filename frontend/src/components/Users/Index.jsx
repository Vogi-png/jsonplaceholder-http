import { useState } from 'react';
import { listarUsuarios, buscarUsuarioPorId, textoErro } from '../../Api.jsx';

export default function Users() {
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

  const filtrarDadosUsuario = (usuario) => ({
    id: usuario.id,
    name: usuario.name,
    email: usuario.email,
    city: usuario.address?.city,
  });

  async function buscar() {
    const id = prompt('ID do usuário:');
    if (!id) return;

    executar(async () => {
      const resposta = await buscarUsuarioPorId(id);
      resposta.data = filtrarDadosUsuario(resposta.data);
      return resposta;
    });
  }

  async function listar() {
    executar(async () => {
      const resposta = await listarUsuarios();
      resposta.data = resposta.data.map(filtrarDadosUsuario);
      return resposta;
    });
  }

  return (
    <section>
      <h2>Usuários</h2>
      <button onClick={listar}>Listar</button>
      <button onClick={buscar}>Buscar por ID</button>

      {status && <p>{status}</p>}
      {resultado && <pre>{JSON.stringify(resultado, null, 2)}</pre>}
    </section>
  );
}