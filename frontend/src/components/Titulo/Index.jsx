// Recebe "escolher" de quem o usa (o App) e chama quando clica
export default function Titulo({ escolher }) {
  return (
    <header>
      <h1>Sistema conectado ao Jsonplaceholder</h1>
      <button onClick={() => escolher('usuarios')}>Usuários</button>
      <button onClick={() => escolher('posts')}>Posts</button>
    </header>
  );
}