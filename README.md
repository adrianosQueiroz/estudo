# Dominando Ambientes Virtuais no Python 🚀

Este projeto demonstra como criar, ativar e gerenciar Ambientes Virtuais (`venv`), uma prática essencial para qualquer desenvolvedor que busca maturidade em Python, especialmente em fluxos de Data Analytics, Automação e Engenharia de Dados.

## 📋 Por que usar Ambientes Virtuais?

No dia a dia de projetos de dados (ETLs, Dashboards, Integrações via n8n), o uso do `venv` é indispensável por três motivos:

1.  **Isolamento de Dependências:** Evita que a atualização de uma biblioteca no "Projeto A" quebre o funcionamento do "Projeto B".
2.  **Reprodutibilidade:** Garante que qualquer pessoa (ou servidor) consiga rodar seu código instalando exatamente as mesmas versões que você utilizou.
3.  **Boas Práticas de Git:** Impede que arquivos pesados da instalação do Python sejam enviados para o GitHub, mantendo o repositório leve (enviamos apenas o código e o arquivo `requirements.txt`).

## 🛠️ Guia Prático: Como replicar este projeto

## Criar o Ambiente Virtual (venv)
No terminal, dentro da pasta do projeto, execute:
python -m venv venv

**1. Ativar o Ambiente Virtual - 
Windows (PowerShell):**

.\venv\Scripts\Activate.ps1

**Windows (Prompt de Comando / CMD):**

**DOS:**
.\venv\Scripts\activate

**Linux/Mac/Git Bash:**
source venv/Scripts/activate


**2. Instalar as Dependências**
Com o ambiente ativo (você verá um (venv) no terminal), instale as bibliotecas necessárias:

pip install requests beautifulsoup4 pandas
Dica Extra para o seu Portfólio:
Se você quiser ser ainda mais profissional, após instalar tudo, rode este comando no terminal: pip freeze > requirements.txt

Isso criará um arquivo chamado requirements.txt. Aí, você pode substituir o passo 2 por:

pip install -r requirements.txt

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/adrianosQueiroz/python-venv-dominio.git](https://github.com/adrianosQueiroz/python-venv-dominio.git)


*Projeto desenvolvido por **Adriano Soares**, unindo experiência em logística e análise de dados.*
