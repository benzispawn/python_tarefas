# Gerenciador de Tarefas

## Sobre o Projeto

Este projeto é um gerenciador de tarefas simples criado com Flask e PostgreSQL, e foi containerizado com Docker para facilitar o desenvolvimento e a implantação. O objetivo é ajudar usuários a criar, visualizar, atualizar e remover tarefas de maneira prática.

## Funcionalidades

- **Criar Tarefa**: Adicione uma nova tarefa com título e descrição.
- **Visualizar Tarefas**: Veja todas as tarefas criadas.
- **Atualizar Tarefa**: Edite o título, a descrição e o status de conclusão.
- **Excluir Tarefa**: Remova tarefas quando necessário.

## Como Executar o Projeto

### Pré-requisitos

- Docker e Docker Compose instalados

### Passo a Passo

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   cd seu_repositorio
2. Crie um arquivo .env para armazenar variáveis de ambiente:

  ```bash
  DATABASE_URL=postgresql://postgres:postgres@db:5432/tasks_db
  FLASK_ENV=production
  SECRET_KEY=sua_chave_secreta
  POSTGRES_USER=postgres
  POSTGRES_PASSWORD=postgres
  POSTGRES_DB=tasks_db
  ```

3. Inicie os containers com Docker Compose:
    
    ```
   docker compose up --build -d
   ```

4. Acesse a aplicação em seu navegador em http://localhost:5000.

### Estrutura do Projeto
## Estrutura do Projeto

- **app/**: Diretório principal da aplicação Flask.
  - **models.py**: Define os modelos do banco de dados e as tabelas utilizadas na aplicação.
  - **routes.py**: Contém as rotas da aplicação para criar, visualizar, atualizar e remover tarefas.
  - **templates/**: Arquivos HTML para renderização das páginas da aplicação.
  - **static/**: Arquivos de estilo (CSS), scripts (JS) e outros recursos estáticos.
- **config.py**: Arquivo de configuração que carrega variáveis de ambiente, como a URL do banco de dados.
- **Dockerfile**: Instruções para criar a imagem Docker da aplicação Flask.
- **docker-compose.yml**: Configuração do Docker Compose para orquestrar os serviços da aplicação, incluindo Flask e PostgreSQL.
- **requirements.txt**: Lista de dependências da aplicação para instalação no ambiente Docker.
- **.env**: Arquivo com variáveis de ambiente sensíveis (não incluído no repositório por segurança).

## Exemplo em Vídeo

### 📹 Demonstração

Clique na imagem abaixo para assistir ao vídeo explicativo sobre o funcionamento da aplicação:

[Clique aqui para assistir ao vídeo](exemplo.webm)
