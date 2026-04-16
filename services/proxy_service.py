# services/proxy_service.py
import httpx
import logging
from fastapi import HTTPException, status
from core.config import settings
from urllib.parse import urlparse
from typing import Optional, Dict

logger = logging.getLogger(__name__)

class ProxyService:
    @staticmethod
    def _is_domain_allowed(url: str) -> bool:
        domain = urlparse(url).netloc
        return any(allowed in domain for allowed in settings.ALLOWED_DOMAINS)

    @classmethod
    async def forward_request(
        cls, 
        method: str, 
        target_url: str, 
        headers: Dict[str, str], 
        json_data: Optional[dict] = None, 
        xml_data: Optional[str] = None,
        timeout: int = 60
    ) -> httpx.Response:
        
        if not target_url:
            raise HTTPException(status_code=400, detail="X-Target-Url header is missing")

        if not cls._is_domain_allowed(target_url):
            logger.warning(f"Blocked request to unauthorized domain: {target_url}")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Target domain is not in the allowed list."
            )

        # Remove our custom headers before forwarding
        clean_headers = {k: v for k, v in headers.items() if k.lower() not in ['host', 'x-target-url', 'x-api-key', 'content-length']}

        async with httpx.AsyncClient(timeout=timeout) as client:
            try:
                logger.info(f"Forwarding {method} request to {target_url}")
                content = xml_data.encode('utf-8') if xml_data else None

                response = await client.request(
                    method=method.upper(),
                    url=target_url,
                    headers=clean_headers,
                    json=json_data,
                    content=content
                )
                return response

            except httpx.RequestError as exc:
                logger.error(f"HTTP Request failed: {exc}")
                raise HTTPException(
                    status_code=status.HTTP_502_BAD_GATEWAY,
                    detail=f"Error communicating with target server: {str(exc)}"
                )