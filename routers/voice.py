# routers/voice.py

import os
import uuid
import shutil
from tempfile import NamedTemporaryFile
from fastapi import (
    APIRouter,
    Request,
    UploadFile,
    File,
    Form,
    HTTPException,
    status
)
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

# This router will be included in the main app
router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Define the output directory for audio files
OUTPUT_DIR = "static/audio"
os.makedirs(OUTPUT_DIR, exist_ok=True)


@router.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    """
    Renders the main page.
    It now uses the cached voices from the application state.
    """
    # Access voices from the app's state (cached on startup)
    # from main import app_state # No longer needed if voices are not fetched from ElevenLabs
    
    # voices = app_state.get("voices", []) # No longer needed if voices are not fetched from ElevenLabs
    # if not voices:
    #     # Provide a graceful message if voices couldn't be loaded
    #     return templates.TemplateResponse(
    #         "index.html",
    #         {"request": request, "voices": [], "error": "Could not load voices from ElevenLabs. Please check API key and connectivity."}
    #     )

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "voices": [], "error": None} # Always return empty voices and no error
    )


@router.post("/convert", response_class=JSONResponse)
async def convert_voice(
    request: Request,
    audio_file: UploadFile = File(...),
    voice_id: str = Form(...)
):
    """
    Handles the voice conversion process.
    - Fixes the core logic to use Speech-to-Speech.
    - Secures file handling.
    - Adds comprehensive error handling.
    """
    # 1. Security: Check for valid audio file type
    if not audio_file.content_type.startswith("audio/"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type. Please upload an audio file."
        )

    try:
        # Access the cached client from app state
        # from main import app_state # No longer needed
        # client = app_state.get("client") # No longer needed
        
        # if not client:
        #     raise HTTPException(
        #         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        #         detail="ElevenLabs client not available. Please check API key configuration."
        #     )

        # 2. Secure File Handling: Use a temporary file to avoid security risks
        with NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            shutil.copyfileobj(audio_file.file, temp_file)
            temp_filepath = temp_file.name

        # 3. Core Logic Fix: Use Speech-to-Speech (STS)
        print(f"Voice conversion functionality is currently disabled.")
        
        # converted_audio_bytes = client.speech_to_speech.convert(
        #     audio=f,
        #     voice_id=voice_id,
        # ) # Commented out ElevenLabs API call

        # For now, we'll just return the original audio as converted, or an error.
        # In a real scenario, you'd integrate a new voice generation service here.
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="Voice conversion service is currently not implemented. Please check back later."
        )

        # 4. Security: Generate a secure, random filename for the output
        # secure_filename = f"converted_{uuid.uuid4()}.mp3"
        # output_filepath = os.path.join(OUTPUT_DIR, secure_filename)

        # 5. Save the converted audio
        # with open(output_filepath, "wb") as output_file:
        #     for chunk in converted_audio_bytes:
        #         output_file.write(chunk)
        # print(f"Saved converted audio to {output_filepath}")

        # 6. Clean up the temporary input file
        # os.remove(temp_filepath)

        # return JSONResponse(
        #     content={
        #         "success": True,
        #         "url": f"/{output_filepath}"
        #     }
        # ) # Commented out success response

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}"
        )
    finally:
        # Ensure the uploaded file buffer is closed
        await audio_file.close()


