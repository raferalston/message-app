# Для запуска используйте докер
docker-compose up -d --build
docker-compose exec web python manage.py migrate
docker compose up

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
