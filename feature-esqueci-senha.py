import hashlib

def recuperar_senha(usuario, nova_senha, banco_usuarios):
    """Simula a alteração de senha de um usuário no dicionário."""
    if usuario in banco_usuarios:
        # Criptografa a nova senha antes de salvar
        banco_usuarios[usuario] = hashlib.sha256(nova_senha.encode('utf-8')).hexdigest()
        print(f"✅ Senha do usuário '{usuario}' redefinida com sucesso de forma segura!")
        return True
    else:
        print("❌ Erro: Usuário não encontrado no sistema.")
        return False