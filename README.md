# 🚀 Alura Space - Galeria de Fotos do Espaço

Uma galeria web completa para exibir e gerenciar fotografias do espaço, desenvolvida com Django. O projeto permite visualizar imagens astronômicas organizadas por categorias como nebulosas, estrelas, galáxias, planetas e satélites.

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Como Usar](#como-usar)
- [Contribuição](#contribuição)
- [Licença](#licença)

## 🎯 Sobre o Projeto

O **Alura Space** é uma aplicação web que oferece uma experiência imersiva para explorar fotografias do espaço. Desenvolvido como parte de um curso da Alura, o projeto demonstra boas práticas de desenvolvimento web com Django, incluindo:

- Interface responsiva e moderna
- Sistema de busca por nome
- Organização por tags/categorias
- Upload e gerenciamento de imagens
- Painel administrativo completo

## ✨ Funcionalidades

### 🖼️ Galeria de Fotos
- Visualização de fotografias em cards organizados
- Imagens organizadas por data de publicação
- Suporte a diferentes formatos de imagem
- Fallback para imagem padrão quando não há foto

### 🔍 Sistema de Busca
- Busca por nome da fotografia
- Filtros por tags (Nebulosa, Estrela, Galáxia, Planeta, Satélite)
- Resultados em tempo real

### 📱 Interface Responsiva
- Design moderno e intuitivo
- Navegação por categorias
- Layout adaptável para diferentes dispositivos
- Ícones e elementos visuais otimizados

### ⚙️ Painel Administrativo
- Cadastro e edição de fotografias
- Controle de publicação (publicar/ocultar)
- Upload de imagens
- Gerenciamento de metadados

## 🛠️ Tecnologias Utilizadas

### Backend
- **Django 5.2.3** - Framework web Python
- **Python 3.x** - Linguagem de programação
- **SQLite** - Banco de dados (desenvolvimento)

### Frontend
- **HTML5** - Estrutura das páginas
- **CSS3** - Estilização e layout
- **JavaScript** - Interatividade (quando necessário)

### Dependências
- `asgiref==3.8.1` - Interface ASGI
- `python-dotenv==1.1.0` - Gerenciamento de variáveis de ambiente
- `sqlparse==0.5.3` - Parser SQL
- `tzdata==2025.2` - Dados de fuso horário

## 📁 Estrutura do Projeto

```
alura-space/
├── galeria/                 # App principal
│   ├── models.py           # Modelo Fotografia
│   ├── views.py            # Views da aplicação
│   ├── urls.py             # URLs do app
│   ├── admin.py            # Configuração do admin
│   └── migrations/         # Migrações do banco
├── setup/                  # Configurações do projeto
│   ├── settings.py         # Configurações Django
│   ├── urls.py             # URLs principais
│   └── static/             # Arquivos estáticos
├── templates/              # Templates HTML
│   └── galeria/
│       ├── base.html       # Template base
│       ├── index.html      # Página inicial
│       ├── image.html      # Página da imagem
│       ├── buscar.html     # Página de busca
│       └── partials/       # Partials do template
├── static/                 # Arquivos estáticos
│   ├── assets/             # Recursos (imagens, ícones)
│   └── styles/             # Arquivos CSS
├── media/                  # Upload de imagens
├── requirements.txt        # Dependências Python
└── manage.py              # Script de gerenciamento Django
```

## 🚀 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git (para clonar o repositório)

### Passos para Instalação

1. **Clone o repositório**
   ```bash
   git clone <url-do-repositorio>
   cd alura-space
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **Linux/Mac:**
   ```bash
   source venv/bin/activate
   ```

4. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuração

1. **Configure as variáveis de ambiente**
   
   Crie um arquivo `.env` na raiz do projeto:
   ```env
   SECRET_KEY=sua_chave_secreta_aqui
   DEBUG=True
   ```

2. **Execute as migrações**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Crie um superusuário (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

4. **Execute o servidor de desenvolvimento**
   ```bash
   python manage.py runserver
   ```

5. **Acesse a aplicação**
   
   Abra seu navegador e acesse: `http://127.0.0.1:8000/`

## 📖 Como Usar

### 👤 Usuário Final

1. **Navegar pela Galeria**
   - Acesse a página inicial para ver todas as fotografias
   - Use as tags para filtrar por categoria
   - Clique em uma imagem para ver detalhes

2. **Buscar Fotografias**
   - Use a barra de busca para encontrar fotos por nome
   - Os resultados são exibidos em tempo real

3. **Visualizar Detalhes**
   - Clique em qualquer imagem para ver informações completas
   - Visualize nome, legenda, descrição e data da fotografia

### 🔧 Administrador

1. **Acessar o Painel Admin**
   - Acesse: `http://127.0.0.1:8000/admin/`
   - Faça login com suas credenciais

2. **Gerenciar Fotografias**
   - Adicione novas fotografias
   - Edite informações existentes
   - Controle a publicação (publicar/ocultar)
   - Faça upload de imagens

3. **Configurar Metadados**
   - Defina nome, legenda e descrição
   - Selecione a categoria (tag)
   - Configure a data da fotografia

## 🎨 Modelo de Dados

### Fotografia
- **nome**: Nome da fotografia (CharField, obrigatório)
- **legenda**: Legenda curta (CharField, obrigatório)
- **descricao**: Descrição detalhada (TextField, obrigatório)
- **tag**: Categoria (choices: Nebulosa, Estrela, Galáxia, Planeta, Satélite)
- **foto**: Arquivo de imagem (ImageField, opcional)
- **publicada**: Status de publicação (BooleanField, padrão: False)
- **data_fotografia**: Data da fotografia (DateTimeField, padrão: agora)

## 🔧 Desenvolvimento

### Estrutura de Views
- `index()`: Exibe a galeria principal
- `image(foto_id)`: Exibe detalhes de uma imagem específica
- `buscar()`: Implementa a funcionalidade de busca

### URLs Principais
- `/`: Página inicial (galeria)
- `/imagem/<id>`: Página de detalhes da imagem
- `/buscar`: Página de busca
- `/admin/`: Painel administrativo

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto foi desenvolvido como parte de um curso da Alura. Sinta-se livre para usar, modificar e distribuir conforme necessário.

## 👨‍💻 Autor

Desenvolvido durante o curso de Django da Alura.

---

**⭐ Se este projeto foi útil para você, considere dar uma estrela!** 
