dev:
	poetry run python manage.py runserver
start:
	poetry run gunicorn -w 5 task_manager.wsgi
install:
	poetry install
check:
	poetry check
lint:
	poetry run flake8
migrate: makemigrate migratedj

migratedj:
	poetry run python manage.py migrate
makemigrate:
	poetry run python manage.py makemigrations task_manager
test:
	poetry run python manage.py test task_manager

