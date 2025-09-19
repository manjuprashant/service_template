from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from starlette.responses import JSONResponse
from .health import router as health_router
from .metrics import setup_metrics, REQUEST_COUNT
from .logging_config import setup_logging
from .auth.jwt import get_current_user, create_access_token

app = FastAPI(title="Service API", version="1.0.0")

setup_logging()
setup_metrics(app)

app.include_router(health_router, prefix="")

class User(BaseModel):
    id: str
    email: str
    full_name: str

fake_db = {
    "users": [
        {"id": "11111111-1111-1111-1111-111111111111", "email": "alice@example.com", "full_name": "Alice Example"}
    ]
}

@app.get("/users", response_model=list[User])
def list_users(page: int = 1):
    return fake_db["users"]

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: str):
    for u in fake_db["users"]:
        if u["id"] == user_id:
            return u
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/token")
def token():
    # demo token endpoint
    token = create_access_token({"sub": "11111111-1111-1111-1111-111111111111"})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/me")
def me(user: dict = Depends(get_current_user)):
    return user

