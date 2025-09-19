from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/health")
def health():
    return JSONResponse({"status": "ok"})

@router.get("/ready")
def ready():
    # Add readiness checks here (DB, cache)
    return JSONResponse({"status": "ready"})
