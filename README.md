# FastAPI Gemini Chat API

A simple FastAPI project integrating with Google's Gemini AI model. This project demonstrates how to build a backend API that interacts with an external AI model while implementing basic rate limiting and authentication.

## Features

- FastAPI-based REST API
- `/chat` endpoint for AI-generated responses
- Rate limiting for authenticated and unauthenticated users
- JWT-based optional authentication
- Integration with Google's Gemini AI (`gemini-2.5-flash-preview-05-20`)
- Environment variable configuration via `.env`
- Docker-ready for easy deployment

## Project Structure

```
src/
├─ main.py # FastAPI application
├─ models.py # Pydantic models for request/response
├─ gemini.py # Gemini API wrapper
├─ throttling.py # Rate limiting logic
└─ dependencies.py # JWT authentication dependencies
.env # Environment variables (API keys, rate limits)
requirements.txt # Python dependencies
Dockerfile # Docker configuration
```

## Setup

1. Get your Gemini API key:

```bash
https://aistudio.google.com
```

2. Clone this repository:

```bash
git clone https://github.com/snushev/fastapi-gemini
cd fastapi-gemini
```

3. Create a `.env` file with the following keys:

```ini
GEMINI_API_KEY=your_gemini_api_key
SECRET_KEY=your_jwt_secret
ALGORITHM=HS256
GLOBAL_RATE_LIMIT=10
GLOBAL_TIME_WINDOW_SECONDS=60
AUTH_RATE_LIMIT=20
AUTH_TIME_WINDOW_SECONDS=60
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run locally:

```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

6. Or run with Docker:

```bash
docker build -t fastapi-gemini .
docker run -p 8000:8000 fastapi-gemini
```

## Next Steps / Potential Improvements

- Add full authentication flow (login, register) to track user usage
- Store chat history in a database
- Add WebSocket support for streaming AI responses
- Extend rate limiting by IP or endpoint
- Add frontend interface (React/Vue) for live chat
- Implement caching for repeated prompts

## License

MIT License
