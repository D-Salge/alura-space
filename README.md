Alura Space
Bem-vindo ao Alura Space, uma aplicação web de galeria de fotos desenvolvida com Django. Este projeto permite que os usuários se cadastrem, façam login, visualizem e gerenciem uma coleção de fotografias. A aplicação é projetada para ser uma plataforma simples e elegante para exibir imagens, com integração ao Amazon S3 para armazenamento de arquivos de mídia.

📖 Índice
Funcionalidades Principais

Tecnologias Utilizadas

Guia de Instalação e Execução

Estrutura do Projeto

✨ Funcionalidades Principais
Autenticação de Usuário: Sistema completo de cadastro, login e logout.

Galeria de Imagens: Visualização de todas as fotografias publicadas na página inicial.

Gerenciamento de Fotos: Usuários autenticados podem adicionar, editar e excluir suas próprias fotografias.

Visualização Detalhada: Página dedicada para cada imagem.

Armazenamento em Nuvem: Integração com o Amazon S3 para hospedar os arquivos de imagem de forma segura e escalável.

Interface Administrativa: Painel de administração do Django para gerenciamento avançado.

🛠️ Tecnologias Utilizadas
Backend:

Python 3

Django 4.1

Frontend:

HTML5

CSS3

Banco de Dados:

SQLite 3 (padrão para desenvolvimento)

Armazenamento de Mídia:

Amazon S3

django-storages

boto3

Gerenciamento de Ambiente:

python-dotenv

🚀 Guia de Instalação e Execução
Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

1. Pré-requisitos
Python 3.8 ou superior

pip (gerenciador de pacotes do Python)

2. Clone o Repositório
Bash

git clone https://github.com/seu-usuario/alura-space.git
cd alura-space
3. Crie e Ative um Ambiente Virtual (venv)
É uma boa prática isolar as dependências do projeto.

No Windows:

Bash

python -m venv venv
venv\Scripts\activate
No macOS/Linux:

Bash

python3 -m venv venv
source venv/bin/activate
4. Instale as Dependências
Instale todas as bibliotecas necessárias listadas no arquivo requirements.txt.

Bash

pip install -r requirements.txt
5. Configure as Variáveis de Ambiente
Crie um arquivo chamado .env na raiz do projeto (na mesma pasta que o manage.py) e adicione as seguintes variáveis:

Snippet de código

# Chave secreta para o Django (gere uma nova e única para você)
SECRET_KEY='sua-secret-key-super-secreta-aqui'

# Credenciais do seu bucket S3 na AWS
AWS_ACCESS_KEY_ID='sua-access-key-id'
AWS_SECRET_ACCESS_KEY='sua-secret-access-key'
AWS_STORAGE_BUCKET_NAME='nome-do-seu-bucket'
AWS_S3_REGION_NAME='regiao-do-seu-bucket' # ex: us-east-1
6. Aplique as Migrações do Banco de Dados
Este comando cria as tabelas do banco de dados necessárias para a aplicação.

Bash

python manage.py migrate
7. Crie um Superusuário
Você precisará de um superusuário para acessar o painel de administração do Django.

Bash

python manage.py createsuperuser
Siga as instruções para criar seu usuário e senha.

8. Execute o Servidor de Desenvolvimento
Com tudo configurado, inicie o servidor local.

Bash

python manage.py runserver
Acesse o projeto em seu navegador no endereço http://127.0.0.1:8000/.

📁 Estrutura do Projeto
O projeto segue a estrutura padrão do Django, com uma clara separação de responsabilidades:

├── apps/                    # Contêiner para as aplicações do projeto
│   ├── galeria/             # App para gerenciar a galeria, fotos, etc.
│   └── usuarios/            # App para gerenciar usuários, login, cadastro
├── setup/                   # Pasta de configuração principal do projeto
│   ├── settings.py          # Arquivo principal de configurações
│   ├── urls.py              # Arquivo principal de URLs
│   └── ...
├── templates/               # Templates HTML globais
├── static/                  # Pasta para arquivos estáticos coletados (gerada)
├── .env                     # Arquivo com variáveis de ambiente (local)
├── manage.py                # Utilitário de linha de comando do Django
└── requirements.txt         # Lista de dependências Python
