В проекте не реализовано логирование и большинство из дополнительных пунктов. 
Я решил сначала сделать базовый функционал + простые тесты, что бы посмотреть сколько времени это займет и соотнести с временем указанным в ТЗ. Результат это то что у меня получилось сделать в течение 5ти часов. 

# Для запуска используйте докер
- docker-compose up -d --build
- docker-compose exec web python manage.py migrate
- docker-compose exec web python manage.py createsuperuser
- docker compose up

## Troubleshooting
Если будет ошибка "exec /app/entrypoint.sh: no such file or directory", тогда необходимо поменять end of line sequence с CRLF на LF, у файла entrypoint.sh

## Extra
Апи не поддерживает локализацию по таймзоне, поэтому может отличаться время создания. *Для проверки функционала можно использовать админку для начала.

## Ссылки
localhost:8000
- /api/ 
> Входная точка
- /clients/ 
> CRUD для клиентов
- /messages/
> CRUD для рассылки
- /messages-statistics/<int:pk>
> read-only для статистики
