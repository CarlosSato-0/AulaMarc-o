import hashlib
import getpass

# Banco de dados temporário
banco_usuarios = {}
usuario_logado = None


def criptografar_senha(senha):
    """Transforma a senha em texto plano em um hash SHA-256 seguro."""
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()


def cadastrar():
    print("\n--- TELA DE CADASTRO ---")
    usuario = input("Digite um nome de usuário: ").strip().lower()

    if usuario in banco_usuarios:
        print("❌ Erro: Este usuário já existe!")
        return

    senha = getpass.getpass("Digite sua senha: ")
    confirmar = getpass.getpass("Confirme sua senha: ")

    if senha != confirmar:
        print("❌ As senhas não coincidem!")
        return

    if len(senha) < 8:
        print("❌ Erro de Segurança: A senha deve ter pelo menos 8 caracteres!")
        return

    banco_usuarios[usuario] = criptografar_senha(senha)
    print("✅ Usuário cadastrado com sucesso!")


def login():
    global usuario_logado
    print("\n--- TELA DE LOGIN ---")
    usuario = input("Usuário: ").strip().lower()
    senha = getpass.getpass("Senha: ")

    senha_salva_hash = banco_usuarios.get(usuario)

    if senha_salva_hash and senha_salva_hash == criptografar_senha(senha):
        usuario_logado = usuario
        print(f"🔓 Acesso liberado! Bem-vindo, {usuario}.")
    else:
        print("❌ Erro: Usuário ou senha incorretos.")


def logout():
    global usuario_logado
    if usuario_logado:
        print(f"🔒 Usuário {usuario_logado} desconectado.")
        usuario_logado = None
    else:
        print("⚠️ Nenhum usuário está logado.")


def listar_usuarios():
    print("\n--- LISTA DE USUÁRIOS ---")
    if banco_usuarios:
        for u in banco_usuarios.keys():
            print(f"- {u}")
    else:
        print("Nenhum usuário cadastrado ainda.")


# Sistema Principal (Menu em Loop)
while True:
    print("\n=========================")
    print("      SAFE LOGIN MENU    ")
    print("=========================")
    print("1. Cadastrar Novo Usuário")
    print("2. Fazer Login")
    print("3. Logout")
    print("4. Listar Usuários")
    print("5. Sair")

    opcao = input("Escolha uma opção (1/2/3/4/5): ").strip()

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        login()
    elif opcao == "3":
        logout()
    elif opcao == "4":
        listar_usuarios()
    elif opcao == "5":
        print("Saindo do sistema... Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")
