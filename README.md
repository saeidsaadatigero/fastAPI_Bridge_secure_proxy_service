# FastAPI Secure Egress Proxy

A production-grade reverse proxy service built with **FastAPI**, designed to securely forward HTTP requests to allowlisted domains with API key authentication.

## Features
- API Key authentication via request header
- Domain-based allowlist enforcement
- Supports JSON and XML forwarding
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

| Method | Endpoint | Auth |
|--------|----------|------|
| POST | `/api/v1/forward` | x-api-key header |
| GET | `/api/v1/health` | Public |
