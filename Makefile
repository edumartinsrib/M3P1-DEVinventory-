install:
	poetry install

db:
	@echo "Configuring database..."
	poetry run flask db init
	poetry run flask db migrate
	poetry run flask db upgrade
	@echo "Database configured."
	@echo "Populating database..."
	poetry run flask populate_db

test:
	poetry run pytest -v --cov-report term-missing --cov-report html --cov-branch \
		--cov src/

lint:
	@echo "Running isort"
	poetry run isort .
	@echo "Running black-blue"
	poetry run blue --color .
	@echo "Running flake8"
	poetry run flake8 .

format:
	poetry run isort .
	poetry run blue .