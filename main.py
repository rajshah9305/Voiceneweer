# main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

# from elevenlabs.client import ElevenLabs # Removed ElevenLabs import

from core.config import settings
from routers import voice

# Application state to hold cached data
app_state = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Fetches and caches expensive resources on startup.
    ElevenLabs voice fetching removed as per user request.
    """
    print("Application startup.")
    # try:
    #     # Initialize client here to use in lifespan
    #     client = ElevenLabs(api_key=settings.ELEVENLABS_API_KEY)
    #     app_state["voices"] = client.voices.get_all()
    #     app_state["client"] = client
    #     print("Voices successfully fetched and cached.")
    # except Exception as e:
    #     print(f"Could not fetch voices from ElevenLabs: {e}")
    #     app_state["voices"] = []
    #     app_state["client"] = None
    app_state["voices"] = [] # Initialize voices as empty list
    app_state["client"] = None # Initialize client as None
    yield
    # Clean up resources on shutdown if needed
    print("Shutting down.")


app = FastAPI(lifespan=lifespan)

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include the voice conversion router
app.include_router(voice.router)


