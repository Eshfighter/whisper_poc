from fastapi import FastAPI, UploadFile, File, Query
import os
from datetime import datetime
from transformers import pipeline
import sqlite3

app = FastAPI()

UPLOAD_DIRECTORY = "backend/uploads"

# Ensure the upload directory exists
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

# Load the Whisper model
transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-tiny")

# Database setup
DATABASE = "backend/transcriptions.db"

# Connect to the database (it will be created if it doesn't exist)
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Create the transcriptions table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS transcriptions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL,
    transcription TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()

@app.get("/health")
async def health_check():
    return {"status": "Service is running"}

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    # Ensure unique file name
    file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
    if os.path.exists(file_location):
        base, ext = os.path.splitext(file.filename)
        file_location = os.path.join(UPLOAD_DIRECTORY, f"{base}_{datetime.now().timestamp()}{ext}")
    
    # Save the file
    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())

    # Transcribe the audio file
    transcription_result = transcriber(file_location)
    transcription = transcription_result['text']

    return {"filename": file.filename, "transcription": transcription}

@app.get("/transcriptions")
async def get_transcriptions():
    # Connect to the database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Retrieve all transcriptions
    cursor.execute("SELECT filename, transcription, timestamp FROM transcriptions")
    transcriptions = cursor.fetchall()

    # Close the connection
    conn.close()

    # Format the response
    response = [
        {"filename": row[0], "transcription": row[1], "timestamp": row[2]} for row in transcriptions
    ]

    return response

@app.get("/search")
async def search_transcriptions(filename: str = Query(..., description="The name of the audio file to search for.")):
    # Connect to the database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Query for transcriptions based on the audio file name
    cursor.execute("SELECT filename, transcription, timestamp FROM transcriptions WHERE filename LIKE ?", (f"%{filename}%",))
    transcriptions = cursor.fetchall()

    # Close the connection
    conn.close()

    # Format the response
    response = [
        {"filename": row[0], "transcription": row[1], "timestamp": row[2]} for row in transcriptions
    ]

    return response 