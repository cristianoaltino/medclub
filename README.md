# api-medclub
Meu teste de avaliação da MedClub Django utilizando rest-framework.

## Instalações
- Certificar de instalar o Python3 no computador.

## Depêndencias
1. Criar diretório do projeto

        $ python3 -m venv projeto-medclub-venv
2. Cd no diretório projeto-medclub-venv:

        $ mkdir -p projeto-medclub-venv/src
        $ cd projeto-medclub-venv/src
3. Ativar o ambiente virtual:

        $ source ./bin/activate
4. Instale as dependências necessárias para executar o aplicativo:

        $ pip3 install -r requirements.txt
5. Faça essas migrações funcionarem:

        $ python3 manage.py makemigrations
        $ python3 manage.py migrate

## Executá-lo
1. Inicie o servidor usando este comando simples:

        $ python3 manage.py runserver
2. Agora você pode acessar o serviço API de arquivo em seu navegador usando:

        http://localhost:8000/

## Endpoints
Endpoints disponíveis na API e os métodos HTTP disponíveis são GET, POST, PUT e DELETE

ENDPOINT |HTTP | CRUD | DESCRIÇÃO
-- | -- |-- |--
`auth/login` | POST | CREATE | Cria um novo token para o usuário logado
`auth/user` | GET | READ | Seleciona o usuário logado
`auth/user` | PUT | UPDATE | Atualiza o usuário logado
`auth/logout` | POST | CREATE | Desabilita o token gerado para o usuário
`auth/registration`| POST | CREATE | Cria um novo usuário(vendedor)
`item/?page=valor` | GET | READ | Seleciona todos os itens
`item/:pk` | GET | READ | Pega um único item
`item`| POST | CREATE | Cria um novo item
`item/:pk` | PUT | UPDATE | Atualiza um nove item
`item/:pk` | DELETE | DELETE | Deleta um item
`usuario/?page=valor` | GET | READ | Seleciona todos os clientes
`usuario/:pk` | GET | READ | Pega um único cliente
`usuario`| POST | CREATE | Cria um novo cliente
`usuario/:pk` | PUT | UPDATE | Atualiza um nove cliente
`usuario/:pk` | DELETE | DELETE | Deleta um cliente
`pedido/?page=valor` | GET | READ | Seleciona todos os pedidos
`pedido/:pk` | GET | READ | Pega um único pedido
`pedido`| POST | CREATE | Cria um novo pedido
`pedido/:pk` | PUT | UPDATE | Atualiza um nove pedido
`pedido/:pk` | DELETE | DELETE | Deleta um pedido
