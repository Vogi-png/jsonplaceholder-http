import requests
import platform
import os

url = "https://jsonplaceholder.typicode.com/users"

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

# Realiza uma requisição GET para a url 
def request_get(id_usuario = None):
    if id_usuario == None:
        endereco = url
    else:
        endereco = f"{url}/{id_usuario}"
    resposta = requests.get(endereco, timeout=10)
    print(f'Status Code: {resposta.status_code}') #exibe o status code da requisição 
    resposta.raise_for_status()
    return resposta.json() 

# OPÇÃO 1: Lista todos os usuários
def list_usuarios():
    exibir_titulo('Listar Usuários:')
    usuarios = request_get()
    for usuario in usuarios:
        exibir_usuario(usuario)

# OPÇÃO 2: Busca um usuário específico pelo ID
def get_usuario():
    exibir_titulo('Buscar Usuário por ID:')
    id_usuario = int(input('Digite o ID do usuário que deseja buscar: '))
    
    usuario = request_get(id_usuario)
    exibir_usuario(usuario)

def main():
    while True:
        limpar_tela()
        print('Escolha uma opção:')
        print('1. Listar Usuários')
        print('2. Buscar Usuário por ID')
        print('3. Sair')

        try:
            opcao = int(input('\nDigite o número da opção desejada: '))

            if opcao == 1:
                list_usuarios()
            elif opcao == 2:
                get_usuario()
            elif opcao == 3:
                        limpar_tela()
                        print('Encerrado com sucesso!')
                        break
            else:
                exibir_titulo('Opção inválida!')
        except ValueError: 
            print('\n Opção inválida!')
        except requests.HTTPError:
            print('\n Usuário não encontrado ou erro na API!')

        voltar_menu()
        

if __name__ == '__main__':
    main()