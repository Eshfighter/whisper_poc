# Full-Stack Audio Transcription Service

This project is a full-stack application for transcribing audio files using a React frontend and a FastAPI backend. The backend integrates the Whisper model from Hugging Face for audio transcription and uses SQLite for storing transcriptions.

## Architecture

- **Frontend:** React application running in a Docker container.
- **Backend:** FastAPI application running in a Docker container.
- **Database:** SQLite for storing transcriptions.
- **External Services:** Whisper model from Hugging Face for audio transcription.

## Features

- Upload audio files for transcription.
- View a list of all transcriptions.
- Search transcriptions by audio file name.

## Setup

### Prerequisites

- Docker
- Node.js (for local development)
- Python 3.12 (for local development)

### Backend Setup

1. Navigate to the `backend` directory:

   ```bash
   cd backend
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

5. Alternatively, build and run the Docker container:

   ```bash
   docker build -t fastapi-backend .
   docker run -p 8000:8000 fastapi-backend
   ```

### Frontend Setup

1. Navigate to the `frontend` directory:

   ```bash
   cd frontend
   ```

2. Install the required packages:

   ```bash
   npm install
   ```

3. Run the React application:

   ```bash
   npm start
   ```

4. Alternatively, build and run the Docker container:

   ```bash
   docker build -t react-frontend .
   docker run -p 3000:3000 react-frontend
   ```

## Usage

- Access the frontend at [http://localhost:3000](http://localhost:3000).
- The backend API is available at [http://localhost:8000](http://localhost:8000).

## Testing

### Backend Tests

1. Navigate to the `backend` directory and activate the virtual environment:

   ```bash
   cd backend
   source venv/bin/activate
   ```

2. Run the tests using `pytest`:

   ```bash
   pytest test_main.py
   ```

### Frontend Tests

1. Navigate to the `frontend` directory:

   ```bash
   cd frontend
   ```

2. Run the tests using `npm`:

   ```bash
   npm test
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.