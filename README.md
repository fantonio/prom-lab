# prom-lab

Executar no diretório raiz do projeto os seguinte comando:

`docker-compose up`

# api-django

No diretório raiz do projeto, basta executar o comando 

`docker run -p 8000:8000 -v ${PWD}:/app aluracursos/api-django:1.0 /bin/bash -c "python manage.py migrate; python manage.py runserver 0.0.0.0:8000"` (no Windows)

`docker run -p 8000:8000 -v $(pwd):/app aluracursos/api-django:1.0 /bin/bash -c "python manage.py migrate; python manage.py runserver 0.0.0.0:8000"` (no Linux)

Endpoint /clientes aceita GET e POST.

Para fazer um POST, é necessário passar nome, email e cpf.

```
{
    "nome": "Fabio",
    "email": "emaildofabio@gmail.com",
    "cpf": "12345678910"
}
```

Caso haja números no nome e/ou o cpf esteja em branco, com mais de 11 caracteres e afins, retornará um 422.

A cada 10 requisições do tipo POST, a décima primeira será um 503.

Novos clientes adicionados retornam 201.

Endpoints desconhecidos retornam 404.