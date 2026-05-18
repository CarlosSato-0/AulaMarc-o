def exibir_perfil(usuario, email_cadastrado="nao_informado@email.com"):
    """Simula a exibição do painel de perfil do usuário logado."""
    print("\n===============================")
    print(f"   PAINEL DE PERFIL: {usuario.upper()}   ")
    print("===============================")
    print(f"👤 Usuário: {usuario}")
    print(f"📧 E-mail: {email_cadastrado}")
    print("🔒 Status da Conta: Protegida com SHA-256")
    print("===============================\n")