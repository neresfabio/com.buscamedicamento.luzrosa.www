# Início

Este é um projeto [Django](http://www.djangoproject.com/).

### O que foi feito

Este é um projeto mínimo do Django 5.0. Ele foi criado com estas etapas:

1.  Configuração Inicial

    - Instalar Python:
      Certifique-se de ter o Python instalado (recomenda-se a versão 3.8 ou superior).
    - Criar um Ambiente Virtual:

    ```sh
        python -m venv venv
    ```

    - Para ativar o ambiente:

      - No windows:

      ```sh
      venv\Scripts\activate
      ```

      - No macOS/Linux:

      ```sh
      source venv/bin/activate

      ```

2.  Instalar Django

    - Instalar Django no ambiente virtual:

    ```sh
    pip install django

    ```

3.  Criando Projeto Django
    - Criar um novo projeto Django:
      ```sh
      django-admin startproject myproject
      ```
      Substitua myproject pelo nome do seu projeto.
4.  Configuração do Projeto
    - Navegue para o diretório criado:
    ```sh
        cd myproject
    ```
    - Executar o servidor de desenvolvimento:
    ```sh
        python manage.py runserver
    ```
    Acesse http://127.0.0.1:8000/ no seu navegador para ver a página inicial padrão do Django.
5.  Criar a Aplicação Django
    - Criar uma nova aplicação dentro do projeto:
    ```sh
    django-admin startapp myapp
    ```
    Substitua `myapp` pelo nome da sua aplicação.
6.  Cadastrar o App na pasta do projeto
    No arquivo `myproject/settings.py`, adicione o nome da aplicação na lista `INSTALLED_APPS`:
    ```python
    INSTALLED_APPS = [
    ...
    'myapp',
    ]

    ```

7.  Para começar a desnvolver a Interface:
    - Criar Rotas
    - Criar View
    - Criar Html
