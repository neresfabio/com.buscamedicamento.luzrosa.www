# com.buscamedicamento.luzrosa.www

## Comandos Git

1. Para atualizar sua lista de branches remotas:

    Execute o comando abaixo para atualizar sua lista de branches remotas.
    ```sh
    git fetch
    ```
2. Verifique se a branch developer está listada:

    Execute o comando abaixo para verificar se a branch developer está listada entre as branches remotas.
    ```sh
    git branch -r
    ```
3. Crie e mude para a branch developer:

    Se a branch developer está listada entre as branches remotas, você pode criar uma branch local e mudar para ela ao mesmo tempo usando o comando checkout -b com a opção --track.
    ```sh
    git checkout -b developer origin/developer
    ```
    Este comando faz duas coisas:

    - Cria uma nova branch local chamada developer.
    - Configura a nova branch local para rastrear a branch remota developer do repositório origin.
    ### Verificar a Branch Atual
    Para confirmar que você está na branch developer, você pode usar o comando:
    ```sh
    git branch
    ```
    A saída deve mostrar a branch developer com um asterisco indicando que ela é a branch atual:
    ```css
      main
    * developer
    ```