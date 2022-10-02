install:
	poetry install

test:
	poetry run pytest -s -v --cov-report term-missing --cov-report html --cov-branch \
		--cov src/

lint:
	@echo
	poetry run isort --diff -c .
	@echo
	poetry run flake8 .
	@echo
	poetry run mypy .
	@echo
	poetry run blue --check --diff --color .
	@echo
	poetry run bandit -r src/
	@echo
	poetry run pip-audit

format:
	poetry run isort .
	poetry run blue .