dev:
	poetry run python manage.py runserver
start:
	poetry run gunicorn -w 5 task_manager.wsgi
install:
	poetry install
check:
	poetry check
