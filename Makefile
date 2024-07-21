lint:
	@echo "Running isort"
	@poetry run isort src tests -q || true
	@echo "Running black"
	@poetry run black src tests -q || true
	@echo "Running mypy"
	@poetry run mypy src tests || true
	@echo "Running flake8"
	@poetry run flake8 src tests || true
