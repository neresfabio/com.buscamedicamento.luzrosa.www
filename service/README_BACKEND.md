


<h1 align="center">💻 BACKEND </h1>
<p align="center">
  Este backend, desenvolvido com Django, fornece uma API para gerenciar dados de clientes, remédios, farmácias e usuários. A API permite criar aplicativos web e móveis dinâmicos e responsivos, proporcionando uma experiência de usuário fluida ao buscar medicamentos. Construída com o framework Django Rest Framework, a API é escalável e fácil de manter, facilitando a integração com aplicativos em qualquer frameowrk web ou linguagem de programação.
</p>
<br/>
<h3 align="center">TECNÓLOGIAS USADAS</h2>
<div align="center">

 ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)  ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)/  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
</div>
   

<br/>
<h3>O QUE FOI DESENVOLVIDO</h2>
<ul>
  
- Endpoints para cadastrar e listar remedios
- Endpoints para cadastrar e listar usuarios
- Integração com o Front-end
- Autenticação dos endpoints com JWT

</ul>

<br/>
<h3>METAS SEREM COMPRIDAS</h2>
<ul>
  
  - Migrar para um banco de dados POSTGRESQL
  - Endpoints para listar remédios por farmácias, localização e valores

</ul>


<h2 align="center">COMO UTILIZAR O PROJETO</h2>

### Pré-requisitos

Antes de começar, certifique-se de ter os seguintes pré-requisitos instalados em seu sistema:

1. [Python](https://www.python.org/downloads/) (Python3++).
2. Importante ter o ambiente virtual no seu projeto VirtualEnv 
 ```bash
   # No seu terminal / powershell digite o seguinte comando para baixar a virtualenv
   
     pip install virtualenv
   
   ```
3. Antes de ativar o ambiente virtual é importante configurar o powershell
 ```bash
   # No seu powershell digite o seguinte comando
   
     Set-ExecutionPolicy Unrestricted -Scope Process -Force
   
   ```
### ⚙️🖥️ Configurando o Projeto em sua máquina

1. Clone este repositório em uma pasta na sua máquina localmente:
   ```bash
   # Na pasta selecionada abra com o git bash e cole este código!
   
     https://github.com/neresfabio/com.buscamedicamento.luzrosa.www.git
   
   ```
2. Certifique-se que deu certo e entre na pasta do projeto:
    ```bash
    # 1- Verifique se o projeto foi clonado corretamente:
    # Resultado esperado ( com.buscamedicamento.luzrosa.www/ )
    
      ls

    # 2- Entre na pasta do projeto
    
      cd com.buscamedicamento.luzrosa.www/

    #3- Aproveite e já entra usando o Vscode

      code .

    
   ```
3. Com o projeto aberto você pode ativar/criar o ambiente virtual:
   - Para Windons:
Entre na pasta do projeto e rode os seguintes códigos no terminal:
    ```bash
    #Pelo Prompt de comando
    
    #Criar a VENV
    python -m venv venv
    
    #Ativar a VENV
    .\venv\Scripts\activate.bat
    
    #Atualizar o pip
    python -m pip install --upgrade pip

    #Pelo PowerShell

    #Criar a VENV
    python -m venv venv

    #Ativar a VENV
    .\venv\Scripts\activate ou .\venv\Scripts\activate.ps1

    #Atualizar o pip
    python -m pip install --upgrade pip
    
   ```
   - Para linux:
Entre na pasta do projeto e rode os seguintes códigos no terminal:
    ```bash
    #Criar a VENV 
    python3 -m venv venv

    #Ativar a VENV
    .\venv\bin\activate

    #Atualizar o pip
    python -m pip install --upgrade pip
    
   ```
   - Para Mac:
Entre na pasta do projeto e rode os seguintes códigos no terminal:
    ```bash

    #Criar a VENV
    python -m venv venv

    #Ativar a VENV
    .\venv/bin/activate

    #Atualizar o pip
    python -m pip install --upgrade pip
        
   ```
    
### 🚩 Iniciando o Servidor local
1. No terminal do projeto execute o comando para baixar todas as dependências do projeto:
   ```text
   
   pip install -r requirements.txt
   
   ```
2. Baixe as migrações do banco de dados:
   ```bash
   # Certificar-se de que está no diretório do projeto Django onde o arquivo manage.py está localizado
   
   python manage.py migrate
   
   ```
3. Você poderá criar um Super Usuário:
   ```bash
      # Essa é uma parte opcional mas é impoirtante criar para ter acesso a parte de admin do django
     
      python manage.py createsuperuser
  
      # logo após esse comando vai ser preciso colocar um nome de usuario, email(opcional) e senha.
  
   ```
3. Você poderá iniciar o servidor:
   ```bash
      # Essa é uma parte opcional mas é impoirtante criar para ter acesso a parte de admin do django
     
      python manage.py runserver 800
  
   ```
  O servidor estará acessível em: [http://localhost:800/](http://localhost:800/) 
  
  #### 🚩💻 Endpoints
  <ul> 
  
  - Criar ou listar remédios: [http://localhost:800/api/v1/remedy/](http://localhost:800/api/v1/remedy/) 
  - Criar ou listar usuários: [http://localhost:800/api/v1/users/](http://localhost:800/api/v1/users/)

  </ul>

<br/>
<br/>

3. Você poderá iniciar o servidor:
    
    ```bash
        # METODO POST para cadastrar um Remédio (http://localhost:800/api/v1/remedy/)
        {
            "name": string,
            "description": string,
            "manufacturer": string,
            "value": float,
            "image": string,
        } 
        {
            "name": "Dorflex",
            "description": "Dorflex é muito bom",
            "manufacturer": "PharmBem",
            "value": 5.00,
            "image": "dorflex.png",
        } 
    ```
    ```bash
        # METODO POST para cadastrar um usuário (http://localhost:800/api/v1/users/)
        {
            "name": string,
            "email": string,
            "password": string,
            "phone_number": string,
            "birth_date": string,
        }
        {
            "name": "Dom Pedro I",
            "email": "example@gmail.com",
            "password": "Senh@12345",
            "phone_number": "+55989786577",
            "birth_date": "2001/01/01",
        }
    ```
    
<br/>



<h1 align="center">PROJETO VOLUNTÁRIO PARA UM BEM MAIOR!</h1>

