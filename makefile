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
lint:
	poetry run flake8 --ignore=E501 task_manager
test:
    poetry run python manage.py test
coverage-xml: #start tests code coverage and write report is xml-file for CodeClimate
	poetry run coverage run --source='.' manage.py test task_manager
	poetry run coverage xml