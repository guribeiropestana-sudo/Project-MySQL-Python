import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="usuario"
)
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tbl_usuarios (
               id INT AUTO_INCREMENT PRIMARY KEY,
               nome_usuario VARCHAR(100) NOT NULL,
               idade_usuario INT,
               telefone_usuario VARCHAR(100),
               email_usuario VARCHAR(100))
               """)

print('Sistema iniciado com sucesso! ')

def menu():
        print("""OPÇÕES:
1 - Cadastradar usuario
2 - Listar usuarios
3 - Deletar usuario
4 - Encerrar programa """)
        return


def cadastrar():
    nome = input('Digite o nome: ')

    try:
        idade = int(input('Digite a sua idade: '))
    except ValueError:
        print('Idade inválida!')
            
    telefone = input('Digite o seu telefone: ')
    email = input('Digite o seu e-mail: ')

    sql = 'INSERT INTO tbl_usuarios (nome_usuario, idade_usuario, telefone_usuario, email_usuario) VALUES (%s, %s, %s, %s)'
    cursor.execute(sql,(nome, idade, telefone, email))
    conexao.commit()
    print('Dados cadastrados com sucesso! ')

def listar():
    cursor.execute('SELECT * FROM tbl_usuarios')
    dados = cursor.fetchall()
    
    if not dados:
        print('Nenhum usuario cadastrado.')
        return
    
    for linha in dados:
        print(f'''
----------------------
Id: {linha[0]}
Nome: {linha[1]}
Idade: {linha[2]}
Telefone: {linha[3]}
Email: {linha[4]}
----------------------''')

def deletarUsuario():
    try:
        id_usuario = int(input('Digite o id para deletar: '))
    except ValueError:
        print('Id inválido')
        return

    cursor.execute('SELECT * FROM tbl_usuarios WHERE id = %s', (id_usuario,))
    usuario = cursor.fetchone()

    if usuario is None:
        print('Usuario não encontrado.')
        return
    
    print(f'\nUsuario encontrado:')
    print(f'''
ID: {usuario[0]}
Nome: {usuario[1]}
Idade: {usuario[2]}
Telefone: {usuario[3]}
Email: {usuario[4]}
''')
    
    confirmar = input('Deseja deletar esse usuario? S/N').strip().lower()

    if confirmar == 's':
        cursor.execute('DELETE FROM tbl_usuarios WHERE id = %s', (id_usuario,))
        conexao.commit()

        print('Usuario deletado com sucesso!')
    else:
        print('Operação cancelada.')

while True:
    menu()
    opcao = input('Digite a sua opcão: ')

    if opcao == '1':
        cadastrar()
    if opcao == '2':
        listar()
    if opcao == '3':
        deletarUsuario()
    if opcao == '4':
        print('Obrigado pela escolha! Volte sempre 🤩')
        break

print('Programa encerrado')