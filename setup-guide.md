# Setup Guide

1. Install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Database migrations:
```bash
# placeholder for alembic or similar
echo "run migrations"
```

3. Run development server:
```bash
uvicorn src.main:app --reload --port 8000
```
