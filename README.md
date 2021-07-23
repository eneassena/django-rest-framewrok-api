## Projeto blog api

neste projeto iniciamos uma pequena api com o objetivo de 
praticar o conceito os verbos rest entender como é seu funcionamento
em aplicações.

## tecnologias
no projeto usamos python versão 3.9 e implementamos um framework de api
para django que foi o djangorestframe e alguns módulos que foi bem úteis para
a construção de authentication e permissions em nível de projeto ou de views,
entre as configurações que tivemos usamos o modulo para urls django-cors-headers
que nos permite configurar url padrões da api e diversos recursos que o djangorestframework tem a oferecer.

* Python <a href="http://python.org" >docs</a>
* Rest Framework
* django-cors-headers

# usando o projeto

usamos o `pipenv shell` para ativa o ambiente virtual
> pipenv shell

*Caso não active no windows digite o seguinte `activate`
> activate

se tiver no linux
> $ sudo source activate

para iniciar o server da api:
> python .\manage.py runserver

<p>verá a seguinte saida:</p>
(blogapi) PS C:\programas\treina-web\framework_django\blogapi> py .\manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 23, 2021 - 10:21:17
Django version 2.2.6, using settings 'blog_project.settings'
Starting development server at http://127.0.0.1:8000/       
Quit the server with CTRL-BREAK.

acessando a rota `/swagger-docs/` você verá a documentação da api 
e todas a rotas disponíveis
