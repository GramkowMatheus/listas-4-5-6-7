import csv

class Usuario:
    def __init__(self, nome, sobrenome, data_nascimento, cpf, username, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.username = username
        self.senha = senha
        self.assinaturas = []

    def adicionarAssinatura(self, assinatura):
        self.assinaturas.append(assinatura)

    def cancelarAssinatura(self, idAssinatura):
        if idAssinatura >= 0 and idAssinatura < len(self.assinaturas):
            del self.assinaturas[idAssinatura]

    def exibirDados(self):
        print("Nome:", self.nome)
        print("Sobrenome:", self.sobrenome)
        print("Data de Nascimento:", self.data_nascimento)
        print("CPF:", self.cpf)
        print("Nome de Usuário:", self.username)
        print("Senha:", self.senha)

    def serializar(self):
        return f"{self.nome},{self.sobrenome},{self.data_nascimento},{self.cpf},{self.username},{self.senha}"

    @staticmethod
    def desserializar(dados):
        nome, sobrenome, data_nascimento, cpf, username, senha = dados
        return Usuario(nome, sobrenome, data_nascimento, cpf, username, senha)


class Assinatura:
    def __init__(self, tipo, preco, idUsuario, status):
        self.tipo = tipo
        self.preco = preco
        self.idUsuario = idUsuario
        self.status = status

    def exibirDados(self):
        print("Tipo:", self.tipo)
        print("Preço:", self.preco)
        print("ID do Usuário:", self.idUsuario)
        print("Status:", self.status)

    def serializar(self):
        return f"{self.tipo},{self.preco},{self.idUsuario},{self.status}"

    @staticmethod
    def desserializar(dados):
        tipo, preco, idUsuario, status = dados
        return Assinatura(tipo, preco, idUsuario, status)


def lerUsuarios():
    usuarios = []
    with open('usuarios.csv', 'r') as arquivo:
        leitorCsv = csv.reader(arquivo)
        for linha in leitorCsv:
            usuario = Usuario.desserializar(linha)
            usuarios.append(usuario)
    return usuarios


def lerAssinaturas():
    assinaturas = []
    with open('assinaturas.csv', 'r') as arquivo:
        leitorCsv = csv.reader(arquivo)
        for linha in leitorCsv:
            assinatura = Assinatura.desserializar(linha)
            assinaturas.append(assinatura)
    return assinaturas


def salvarUsuarios(usuarios):
    with open('usuarios.csv', 'w', newline='') as arquivo:
        escritorCsv = csv.writer(arquivo)
        for usuario in usuarios:
            escritorCsv.writerow(usuario.serializar().split(','))


def salvarAssinaturas(assinaturas):
    with open('assinaturas.csv', 'w', newline='') as arquivo:
        escritorCsv = csv.writer(arquivo)
        for assinatura in assinaturas:
            escritorCsv.writerow(assinatura.serializar().split(','))


def adicionarUsuario():
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
    cpf = input("CPF: ")
    username = input("Nome de Usuário: ")
    senha = input("Senha: ")
    usuario = Usuario(nome, sobrenome, data_nascimento, cpf, username, senha)
    return usuario


def adicionarAssinatura(usuario):
    tipo = input("Tipo de Assinatura: ")
    preco = input("Preço: ")
    idUsuario = usuario.cpf
    status = input("Status: ")
    assinatura = Assinatura(tipo, preco, idUsuario, status)
    usuario.adicionarAssinatura(assinatura)


def cancelarAssinatura(usuario):
    idAssinatura = int(input("ID da Assinatura para Cancelar: "))
    usuario.cancelar_assinatura(idAssinatura)


usuarios = lerUsuarios()
assinaturas = lerAssinaturas()

usuarioAtual = None
opcao = ""
while opcao != "sair":
    print("\n--- MENU ---")
    print("1. Fazer login")
    print("2. Cadastrar usuário")
    print("3. Adicionar assinatura")
    print("4. Cancelar assinatura")
    print("5. Exibir dados do usuário")
    print("6. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cpf = input("Digite o CPF do usuário: ")
        for usuario in usuarios:
            if usuario.cpf == cpf:
                usuarioAtual = usuario
                print("Usuário logado com sucesso!")
                break
        else:
            print("Usuário não encontrado.")

    elif opcao == "2":
        novoUsuario = adicionarUsuario()
        usuarios.append(novoUsuario)
        print("Usuário cadastrado com sucesso!")

    elif opcao == "3":
        if usuarioAtual:
            adicionarAssinatura(usuarioAtual)
            print("Assinatura adicionada com sucesso!")
        else:
            print("Faça login primeiro.")

    elif opcao == "4":
        if usuarioAtual:
            cancelarAssinatura(usuarioAtual)
            print("Assinatura cancelada com sucesso!")
        else:
            print("Faça login primeiro.")

    elif opcao == "5":
        if usuarioAtual:
            usuarioAtual.exibirDados()
        else:
            print("Faça login primeiro.")

    elif opcao == "6":
        print("Saindo...")
        salvarUsuarios(usuarios)
        salvarAssinaturas(assinaturas)
        opcao = "sair"

    else:
        print("Opção inválida. Tente novamente.")
