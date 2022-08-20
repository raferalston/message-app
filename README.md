# Foreword
В проекте не реализовано логирование и большинство из дополнительных пунктов. 
Я решил сначала сделать базовый функционал + простые тесты, что бы посмотреть сколько времени это займет и соотнести с временем указанным в ТЗ. Это то что у меня получилось сделать за 5ти часов. 

## Для запуска используйте докер
- docker-compose up -d --build
- docker-compose exec web python manage.py migrate
- docker-compose exec web python manage.py createsuperuser
- docker-compose exec web python manage.py populate_db
- > создаст несколько пользователей в базу с тегами even и odd
- docker compose up

## Тестирование 
- docker-compose exec web python manage.py test
> С запущенным сервером будет вызвана ошибка DoesNotExists, так как тесты не учитывают использование celery/redis. Это можно исправить если использовать mock тестирование

## Troubleshooting
Если будет ошибка "exec /app/entrypoint.sh: no such file or directory", тогда необходимо поменять end of line sequence с CRLF на LF, у файла entrypoint.sh

## Extra
Апи не поддерживает локализацию по таймзоне, поэтому может отличаться время создания. *Для проверки функционала можно использовать админку для начала.

## Links
localhost:8000
> Входная точка
- /api/ 
> CRUD для клиентов
- /clients/
- /clients/int:pk
> CRUD для рассылки
- /messages/
- /messages/int:pk
> read-only для статистики
- /messages-statistics/
- /messages-statistics/int:pk
