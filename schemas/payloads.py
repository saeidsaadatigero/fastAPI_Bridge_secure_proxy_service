# schemas/payloads.py
from pydantic import BaseModel, HttpUrl
from typing import Any, Dict, Optional

class ProxyRequest(BaseModel):
    target_url: HttpUrl
    method: str = "GET"
    headers: Optional[Dict[str, str]] = None
    json_data: Optional[Dict[str, Any]] = None
    xml_data: Optional[str] = None
    timeout: int = 60