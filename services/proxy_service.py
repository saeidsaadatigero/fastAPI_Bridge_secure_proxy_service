# services/proxy_service.py
import httpx
import logging
from fastapi import HTTPException, status
from schemas.payloads import ProxyRequest
from core.config import settings
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

class ProxyService:
    @staticmethod
    def _is_domain_allowed(url: str) -> bool:
        domain = urlparse(url).netloc
        return any(allowed in domain for allowed in settings.ALLOWED_DOMAINS)

    @classmethod
    async def forward_request(cls, request_data: ProxyRequest) -> httpx.Response:
        target_url_str = str(request_data.target_url)

        if not cls._is_domain_allowed(target_url_str):
            logger.warning(f"Blocked request to unauthorized domain: {target_url_str}")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Target domain is not in the allowed list.",
            )

        async with httpx.AsyncClient(timeout=request_data.timeout) as client:
            try:
                logger.info(f"Forwarding {request_data.method} to {target_url_str}")
                content = request_data.xml_data.encode("utf-8") if request_data.xml_data else None
                response = await client.request(
                    method=request_data.method.upper(),
                    url=target_url_str,
                    headers=request_data.headers,
                    json=request_data.json_data,
                    content=content,
                )
                return response
            except httpx.RequestError as exc:
                logger.error(f"HTTP Request failed: {exc}")
                raise HTTPException(
                    status_code=status.HTTP_502_BAD_GATEWAY,
                    detail=f"Error communicating with target server: {str(exc)}",
                )