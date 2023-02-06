dev:
	poetry run python manage.py runserver
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi
install:
	poetry install
check:
	poetry check
lint:
	poetry run flake8
migrate:
	poetry run python manage.py makemigrations task_manager
	poetry run python manage.py migrate
test:
	poetry run python manage.py test task_manager
start2:
	poetry run python manage.py migrate && gunicorn task_manager.wsgi
