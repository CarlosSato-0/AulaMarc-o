import datetime
from typing import Dict
import bcrypt
import jwt
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr

app = FastAPI(title="SafeAuth API", version="1.0.0")

# CONFIGURAÇÕES DE SEGURANÇA (Em produção, use variáveis de ambiente)
SECRET_KEY = "sua_chave_secreta_super_segura_e_longa_aqui"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Simulação de um banco de dados em memória
# ATENÇÃO: Nunca guardamos senhas em texto plano, apenas o hash gerado pelo bcrypt
db_usuarios: Dict[str, dict] = {}

# Define de onde o FastAPI vai extrair o token nas rotas protegidas
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# ---- SCHEMAS DE DADOS (Pydantic) ----
class UsuarioRegistro(BaseModel):
    email: EmailStr
    password: str


class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str


# ---- FUNÇÕES AUXILIARES DE SEGURANÇA ----
def gerar_hash_senha(senha: str) -> str:
    """Gera um hash seguro usando bcrypt (com salting automático)."""
    bytes_senha = senha.encode("utf-8")
    sal = bcrypt.gensalt(rounds=12)  # 12 rounds é um bom equilíbrio entre segurança e performance
    hash_bytes = bcrypt.hashpw(bytes_senha, sal)
    return hash_bytes.decode("utf-8")


def verificar_senha(senha_plana: str, senha_hash: str) -> bool:
    """Verifica se a senha digitada corresponde ao hash salvo."""
    return bcrypt.checkpw(senha_plana.encode("utf-8"), senha_hash.encode("utf-8"))


def criar_token_acesso(dados: dict) -> str:
    """Gera um token JWT com tempo de expiração."""
    dados_para_codificar = dados.copy()
    tempo_expiracao = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    dados_para_codificar.update({"exp": tempo_expiracao})
    token_jwt = jwt.encode(dados_para_codificar, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt


def obter_usuario_atual(token: str = Depends(oauth2_scheme)) -> str:
    """Dependência para proteger rotas. Valida o JWT e extrai o usuário."""
    excecao_credenciais = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido ou expirado.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise excecao_credenciais
        return email
    except jwt.PyJWTError:
        raise excecao_credenciais


# ---- ROTAS (ENDPOINTS) ----


@app.post("/register", status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario: UsuarioRegistro):
    """Rota para cadastrar um novo usuário com senha criptografada."""
    if usuario.email in db_usuarios:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="E-mail já cadastrado."
        )

    # Criptografa a senha antes de salvar
    senha_criptografada = gerar_hash_senha(usuario.password)

    db_usuarios[usuario.email] = {
        "email": usuario.email,
        "password_hash": senha_criptografada,
    }

    return {"message": "Usuário registrado com sucesso seguro!"}


@app.post("/login")
def login(usuario: UsuarioLogin):
    """Rota de autenticação que retorna o Bearer Token se as credenciais forem válidas."""
    usuario_encontrado = db_usuarios.get(usuario.email)

    # Mensagem genérica de erro para evitar enumeração de usuários (boa prática de segurança)
    erro_autenticacao = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="E-mail ou senha incorretos.",
    )

    if not usuario_encontrado:
        raise erro_autenticacao

    # Verifica se a senha bate com o hash
    if not verificar_senha(usuario.password, usuario_encontrado["password_hash"]):
        raise erro_autenticacao

    # Se estiver tudo certo, gera o token JWT
    token_acesso = criar_token_acesso(dados={"sub": usuario.email})

    return {"access_token": token_acesso, "token_type": "bearer"}


@app.get("/me")
def ler_dados_protegidos(email_usuario_atual: str = Depends(obter_usuario_atual)):
    """Rota protegida que só pode ser acessada por usuários autenticados com um token válido."""
    return {
        "mensagem": "Você acessou uma área segura!",
        "usuario_autenticado": email_usuario_atual,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

    