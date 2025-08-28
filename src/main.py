import os
from dotenv import load_dotenv
from fastapi import FastAPI
from .models import ChatRequest, ChatResponse
from .gemini import Gemini
from .throttling import apply_rate_limit

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

ai_platform = Gemini(api_key=gemini_api_key)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API is running"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    apply_rate_limit("global_unauthenticated_user")
    response_text = ai_platform.chat(request.prompt)
    return ChatResponse(response=response_text)