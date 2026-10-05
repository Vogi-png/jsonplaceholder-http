import requests
import platform
import os


URL = "https://jsonplaceholder.typicode.com"


# Limpa a tela do terminal, dependendo do sistema operacional
def limpar_tela():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# Exibe o título de cada seção e limpar a tela antes de mostrar o conteúdo
def exibir_titulo(texto):
    limpar_tela()
    print(texto)
    print()

# Volta ao menu principal após a execução de uma função
def voltar_menu():
    print('\n Aperte qualquer tecla para voltar ao menu principal\n')
    input()

# Formata e exibe as informações do usuário
def exibir_usuario(usuario):
    print(f"[Usuário {usuario['id']}] Name: {usuario['name']} | Email: {usuario['email']} | Cidade: {usuario['address']['city']}")

# Formata e exibe as informações do post
def exibir_post(post):
    print(f"\n[Postagem {post['id']}]\n Feito por Usuário: {post['userId']} | Título: {post['title']} | \nConteúdo: {post['body']}\n\n")

# Realiza uma requisição GET para a url 
def request_get(setor, id_usuario = None, params=None):
    if id_usuario == None:
        endereco = f'{URL}/{setor}'
    else:
        endereco = f'{URL}/{setor}/{id_usuario}'
    resposta = requests.get(endereco, params=params, timeout=10) 
    print(f'Status Code: {resposta.status_code}') #exibe o status code da requisição 
    resposta.raise_for_status()
    return resposta.json() 

# Realiza uma requisição POST para a url
def request_post(setor, data):
    resposta = requests.post(f'{URL}/{setor}', json=data, timeout=10)
    print(f'Status Code: {resposta.status_code}')
    resposta.raise_for_status()
    return resposta.json()

# Realiza uma requisição PATCH para a url
def request_patch(setor, id_post, data):
    resposta = requests.patch(f'{URL}/{setor}/{id_post}', json=data, timeout=10)
    print(f'Status Code: {resposta.status_code}')
    resposta.raise_for_status()
    return resposta.json()

# Realiza uma requisição DELETE para a url
def request_delete(setor, id_post):
    resposta = requests.delete(f'{URL}/{setor}/{id_post}', timeout=10)
    print(f'Status Code: {resposta.status_code}')
    resposta.raise_for_status()

# OPÇÃO 1.1: Lista todos os usuários
def list_usuarios():
    exibir_titulo('Listar Usuários:')
    usuarios = request_get('users')
    for usuario in usuarios:
        exibir_usuario(usuario)

# OPÇÃO 1.2: Lista todos os posts
def list_posts():
    exibir_titulo('Listar Posts:')
    posts = request_get('posts')
    for post in posts:
        exibir_post(post)

# OPÇÃO 2: Busca um usuário específico pelo ID
def get_usuario():
    exibir_titulo('Buscar Usuário por ID:')
    id_usuario = int(input('Digite o ID do usuário que deseja buscar: '))
    usuario = request_get('users', id_usuario)
    exibir_usuario(usuario)

# OPÇÃO 2.2: Busca os posts de um usuário específico pelo ID
def get_post():
    exibir_titulo('Posts de um Usuário:')
    id_usuario = int(input('Digite o ID do usuário: '))
    posts = request_get('posts', params={'userId': id_usuario})
    for post in posts:
        exibir_post(post)

# OPÇÃO 2.3: Cria um novo post para um usuário específico
def post_post():
    exibir_titulo('Criar Post:')
    id_usuario = int(input('Digite o ID do usuário: '))
    titulo = input('Digite o título do post: ')
    conteudo = input('Digite o conteúdo do post: ')
    data = {
        "userId": id_usuario,
        "title": titulo,
        "body": conteudo
    }
    post = request_post('posts', data)
    exibir_post(post)

# OPÇÃO 2.4: Atualiza um post específico pelo ID
def patch_post():
    exibir_titulo('Atualizar Post:')
    id_post = int(input('Digite o ID do post que deseja atualizar: '))
    exibir_post(request_get('posts', id_post))

    confirmacao = input(f'Esse é o post que deseja atualizar? (s/n):')
    if confirmacao.lower() == 's': 
            titulo = input('Digite o novo título do post: ')
            data = {
                "title": titulo,
            }
            post = request_patch('posts', id_post, data)
            exibir_post(post)
    elif confirmacao.lower() == 'n':
        print('Atualização cancelada.')
        return
    else:
        print('Opção inválida.')

# OPÇÃO 2.5: Deleta um post específico pelo ID
def delete_post():
    exibir_titulo('Deletar Post:')
    id_post = int(input('Digite o ID do post que deseja deletar: '))
    exibir_post(request_get('posts', id_post))

    confirmacao = input(f'Tem certeza que deseja deletar esse post? (s/n): ')
    if confirmacao.lower() == 's':
        request_delete('posts', id_post)
        print(f'Post {id_post} deletado com sucesso!')
    elif confirmacao.lower() == 'n':
        print('Ação Cancelada!')
    else:
        print('Opção inválida.')

# Menu de listagem de usuários ou posts
def menu_usuarios():
    limpar_tela()
    print('Escolha uma opção para USUÁRIOS:')
    print('1. Listar Usuários')
    print('2. Buscar Usuário por ID')
    print('0. Voltar')

# Menu de busca de usuários ou posts
def menu_posts():
    limpar_tela()
    print('Escolha uma opção para POSTS:')
    print('1. Listar Posts')
    print('2. Buscar Posts por ID do Usuário')
    print('3. Criar Post')
    print('4. Atualizar Post')
    print('5. Deletar Post')
    print('0. Voltar')

def main():
    while True:
        limpar_tela()
        print('Escolha uma opção:')
        print('1. Usuários')
        print('2. Posts')
        print('0. Sair')

        try:
            opcao = int(input('\nDigite o número da opção desejada: '))

            if opcao == 1:
                menu_usuarios()
                sub_opcao = int(input('Digite o número da opção desejada: '))
                if sub_opcao == 1:
                    list_usuarios()
                elif sub_opcao == 2:
                    get_usuario()
                elif sub_opcao == 0:
                    continue
                else:
                    exibir_titulo('Opção inválida!')
            elif opcao == 2:
                menu_posts()
                sub_opcao = int(input('Digite o número da opção desejada: '))
                if sub_opcao == 1:
                    list_posts()
                elif sub_opcao == 2:
                    get_post()
                elif sub_opcao == 3:
                    post_post() 
                elif sub_opcao == 4:
                    patch_post()
                elif sub_opcao == 5:
                    delete_post()
                elif sub_opcao == 0:
                    continue
                else:
                    exibir_titulo('Opção inválida!')
            elif opcao == 0:
                limpar_tela()
                print('Encerrado com sucesso!')
                break
            else:
                exibir_titulo('Opção inválida!')
        except ValueError: 
            print('\n Opção inválida!')
        except requests.HTTPError:
            print('\n Usuário/Post não encontrado ou erro na API!')
        except requests.RequestException:
            print('\n Não foi possível conectar à API!')

        voltar_menu()
        

if __name__ == '__main__':
    main()