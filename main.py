import hashlib

# FUNCIONALIDADE: Recuperação de senha em desenvolvimento...

# Nosso "banco de dados" temporário (um dicionário simples)
# Ele vai guardar o formato: {"usuario": "senha_criptografada"}
banco_usuarios = {}


def criptografar_senha(senha):
    """Transforma a senha em texto plano em um hash SHA-256 seguro."""
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()


def cadastrar():
    print("\n--- TELA DE CADASTRO ---")
    usuario = input("Digite um nome de usuário: ").strip().lower()

    if usuario in banco_usuarios:
        print("❌ Erro: Este usuário já existe!")
        return

    senha = input("Digite sua senha: ")

    # ---- NOVA VALIDAÇÃO (RESOLVENDO A ISSUE #1) ----
    if len(senha) < 8:
        print("❌ Erro de Segurança: A senha deve ter pelo menos 8 caracteres!")
        return
    # -------------------------------------------------

    banco_usuarios[usuario] = criptografar_senha(senha)
    print("✅ Usuário cadastrado com sucesso de forma segura!")


def login():
    print("\n--- TELA DE LOGIN ---")
    usuario = input("Usuário: ").strip().lower()
    senha = input("Senha: ")

    # Buscamos o hash da senha que está salvo no sistema
    senha_salva_hash = banco_usuarios.get(usuario)

    # Criptografamos a senha que o usuário digitou agora para comparar os hashes
    if senha_salva_hash and senha_salva_hash == criptografar_senha(senha):
        print(f"🔓 Acesso liberado! Bem-vindo, {usuario}.")
    else:
        print("❌ Erro: Usuário ou senha incorretos.")


# Sistema Principal (Menu em Loop)
while True:
    print("\n=========================")
    print("      SAFE LOGIN MENU    ")
    print("=========================")
    print("1. Cadastrar Novo Usuário")
    print("2. Fazer Login")
    print("3. Sair")

    opcao = input("Escolha uma opção (1/2/3): ").strip()

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        login()
    elif opcao == "3":
        print("Saindo do sistema... Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")