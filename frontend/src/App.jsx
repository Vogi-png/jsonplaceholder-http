import { useState } from 'react';
import Titulo from './components/Titulo/Index';
import Users from './components/Users/Index';
import Posts from './components/Posts/Index';

export default function App() {
  // Guarda qual tela está aberta: '', 'usuarios' ou 'posts'
  const [tela, setTela] = useState('');

  return (
    <div>
      {/* Passamos a função setTela para o Titulo, para os botões mudarem a tela */}
      <Titulo escolher={setTela} />

      {tela === 'usuarios' && <Users />}
      {tela === 'posts' && <Posts />}
    </div>
  );
}