dev:
	poetry run python manage.py runserver
migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate
dro_db:
	docker exec postgres_hexlet psql -U sh -c  "DROP DATABASE hexlet;"
create_db:
	docker exec postgres_hexlet psql -U sh -c  "CREATE DATABASE hexlet WITH OWNER = sh;"
