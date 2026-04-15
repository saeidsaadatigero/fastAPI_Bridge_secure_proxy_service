# api/v1/endpoints.py
from fastapi import APIRouter, Depends, Response
from schemas.payloads import ProxyRequest
from services.proxy_service import ProxyService
from core.security import verify_api_key

router = APIRouter()

@router.post("/forward", dependencies=[Depends(verify_api_key)])
async def forward_api_call(payload: ProxyRequest):
    response = await ProxyService.forward_request(payload)
    return Response(
        content=response.content,
        status_code=response.status_code,
        media_type=response.headers.get("content-type", "application/json"),
    )

@router.get("/health")
async def health_check():
    return {"status": "ok", "service": "fastapi-bridge"}