# FastAPI Secure Egress Proxy
<img width="1654" height="855" alt="Screenshot 2026-04-15 161305" src="https://github.com/user-attachments/assets/0518ce40-5d9a-4a99-8bed-21d95b2c4490" />

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
