# api/v1/endpoints.py
from fastapi import APIRouter, Depends, Response, Header, Request
from typing import Optional
from schemas.payloads import ProxyPayload
from services.proxy_service import ProxyService
from core.security import verify_api_key

router = APIRouter()

@router.get("/forward", dependencies=[Depends(verify_api_key)])
async def forward_get_call(request: Request, x_target_url: str = Header(..., alias="X-Target-Url")):
    """Handles GET requests. Reads target URL from header."""
    response = await ProxyService.forward_request(
        method="GET",
        target_url=x_target_url,
        headers=dict(request.headers)
    )
    return Response(
        content=response.content,
        status_code=response.status_code,
        media_type=response.headers.get("content-type", "application/json")
    )

@router.post("/forward", dependencies=[Depends(verify_api_key)])
async def forward_post_call(request: Request, payload: ProxyPayload, x_target_url: str = Header(..., alias="X-Target-Url")):
    """Handles POST requests. Reads target URL from header and data from payload."""
    response = await ProxyService.forward_request(
        method="POST",
        target_url=x_target_url,
        headers=dict(request.headers),
        json_data=payload.json_data,
        xml_data=payload.xml_data
    )
    return Response(
        content=response.content,
        status_code=response.status_code,
        media_type=response.headers.get("content-type", "application/json")
    )

@router.get("/health")
async def health_check():
    return {"status": "ok", "service": "fastapi-bridge"}