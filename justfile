set shell := ["bash", "-uc"]

format:
	black . --exclude=".history/*" --exclude="venv/*" --line-length 79 --preview
	ruff . --fix

install:
	poetry install
	pre-commit install

lint:
	black . --exclude=".history/*" --exclude="venv/*" --line-length 79 --preview
	ruff . --check

pre_commit:
	just format
	pre-commit run --all-files
