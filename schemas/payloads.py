# schemas/payloads.py
from pydantic import BaseModel
from typing import Any, Dict, Optional

# این کلاس فقط برای بدنه (Body) درخواست‌های POST استفاده می‌شود
class ProxyPayload(BaseModel):
    json_data: Optional[Dict[str, Any]] = None
    xml_data: Optional[str] = None