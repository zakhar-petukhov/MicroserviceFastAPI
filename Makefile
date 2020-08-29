GUNICORN = @gunicorn -c gunicorn.conf.py

.PHONY: all $(MAKECMDGOALS)

all: ci

lint:
	flake8 --select=C --exit-zero
	flake8 --extend-ignore=C901

checkformat:
	black --check .
	isort --check .

format:
	black .
	isort .

migrate:
	alembic upgrade head

rollback:
	alembic downgrade -1

migration:
	alembic revision --autogenerate -m "${MESSAGE}"

dev:
	@uvicorn --reload main:app

production:
	$(GUNICORN) main:app

offers:
	$(GUNICORN) offers:app

users:
	$(GUNICORN) users:app

generatekeys:
	@echo "JWT secret is" `python3 -c "import secrets; print(secrets.token_urlsafe(48))"`

ci: checkformat lint