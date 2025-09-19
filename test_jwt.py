from src.auth.jwt import create_access_token, JWT_SECRET
import jwt

def test_jwt_create_and_decode():
    token = create_access_token({"sub": "123"})
    payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
    assert payload.get("sub") == "123"
