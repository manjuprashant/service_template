install-deps:
	python -m pip install -r requirements.txt

run-dev:
	uvicorn src.main:app --reload --port 8000

test-unit:
	pytest tests/unit

test-integration:
	pytest tests/integration

