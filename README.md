# django_rest_api_proj_educ

<details>

<summary>Как запустить это приложение в контейнере?</summary>

* Необходимо установить docker на свою машину:
  https://docs.docker.com/get-docker/

* Далее перейти в папку django_rest_api_proj_educ/ и ввсти код:
  <pre><code>docker-compose build</code></pre>

* После сборки образов "поднять" контейнер:
  <pre><code>docker-compose up</code></pre>

* Далее надо применить миграции в контейнере:
  <pre><code>docker-compose exec app python3 manage.py migrate</code></pre>
 
* Надо создать базу данных:
  <pre><code>docker-compose exec db psql -U postgres</code></pre>
  <pre><code>create database NAME_BD;</code></pre>

</details>
