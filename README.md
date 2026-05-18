# SafeAuth API 🔒

Este é um miniprojeto focado em segurança de backend e boas práticas de autenticação, desenvolvido como parte das atividades práticas de controle de versão utilizando Git e GitHub. O sistema simula um fluxo completo de cadastro e login de usuários via terminal em Python, garantindo que credenciais sensíveis nunca sejam expostas em texto plano.

---

## 🎯 Objetivo do Projeto

O objetivo principal do projeto foi aplicar os conceitos fundamentais de criptografia de senhas utilizando algoritmos de hashing e, em paralelo, consolidar o aprendizado prático do ecossistema Git, incluindo gerenciamento de branches, resolução de tarefas via Issues e integração de código através de Pull Requests (PRs).

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x** – Linguagem base para a construção da lógica de segurança.
* **Hashlib** – Biblioteca nativa para a geração de hashes seguros com o algoritmo SHA-256.
* **Git & GitHub** – Utilizados para versionamento de código, ramificação de funcionalidades e documentação de tarefas.

---

## 🚀 Funcionalidades Implementadas

O projeto foi dividido de forma modular utilizando ramificações específicas (*feature branches*) para cada contexto de desenvolvimento:

### 1. Sistema de Login & Cadastro Seguro (`main.py`)
* **Cadastro de Usuários:** Permite registrar um nome de usuário único.
* **Hashing de Senhas (SHA-256):** Aplica a regra de ouro da segurança, convertendo a senha do usuário em uma string irreconhecível de 64 caracteres antes do armazenamento.
* **Validação de Complexidade (Issue #1):** Sistema de barreira que impede o cadastro de senhas fracas (menores que 8 caracteres).
* **Autenticação Eficiente:** Valida as credenciais comparando o hash da senha digitada com o hash armazenado em memória.

### 2. Recuperação de Senha (`feature-esqueci-senha.py`)
* Módulo isolado projetado para redefinir as credenciais de usuários já existentes no ecossistema, aplicando novamente o mascaramento seguro com SHA-256 após a redefinição.

### 3. Painel de Perfil do Usuário (`perfil.py`)
* Interface simulada que exibe as informações de segurança, e-mail e status da conta do usuário atualmente autenticado no ecossistema.

---

## 💻 Como Executar o Projeto

Para testar o fluxo de autenticação localmente na sua máquina, siga os passos abaixo:

1. Certifique-se de ter o Python instalado.
2. Clone o repositório ou baixe os arquivos na sua máquina:
   ```bash
   git clone [https://github.com/CarlosSato-0/AulaMarc-o.git](https://github.com/CarlosSato-0/AulaMarc-o.git)