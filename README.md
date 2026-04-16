# FastAPI Secure Egress Proxy
<img width="1654" height="855" alt="Screenshot 2026-04-15 161305" src="https://github.com/user-attachments/assets/8f0769e3-5c75-41e7-bedd-3e25a1e52708" />

A production-grade **transparent reverse proxy** built with **FastAPI**, designed to securely forward HTTP requests to allowlisted domains with API key authentication.

## Features
- Transparent proxy: forwards the exact HTTP method (GET→GET, POST→POST)
- API Key authentication via `x-api-key` header
- Target URL passed via `X-Target-Url` header (not in body)
- Domain-based allowlist enforcement
- Supports JSON and XML body forwarding
- Async HTTP client (httpx)
- Clean layered architecture (config / security / service / api)

## Stack
- FastAPI + Uvicorn
- httpx (async HTTP)
- python-decouple (env management)
- Pydantic v2

## Setup

```bash
python -m venv venv
venv\Scripts\activate       # Windows
pip install -r requirements.txt
cp .env.example .env        # fill in your values
uvicorn main:app --reload
```

## API

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/api/v1/forward` | x-api-key | Forward a GET request |
| POST | `/api/v1/forward` | x-api-key | Forward a POST request with JSON/XML body |
| GET | `/api/v1/health` | Public | Health check |

## Request Example

```http
GET /api/v1/forward HTTP/1.1
x-api-key: your_secret_key
X-Target-Url: https://api.example.com/resource
```

```http
POST /api/v1/forward HTTP/1.1
x-api-key: your_secret_key
X-Target-Url: https://api.example.com/resource
Content-Type: application/json

{
  "json_data": { "key": "value" }
}
```
