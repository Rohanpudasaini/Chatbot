# Voice-based Intent Classifier

This project is a voice-powered intent classification application. It uses OpenAI's Whisper to transcribe voice commands and Rasa NLU to understand the user's intent from the transcribed text. The application is built with FastAPI and communicates with the frontend using WebSockets.

## Features

- **Voice-to-Text Transcription:** Utilizes the `openai-whisper` library to convert spoken language into text.
- **Intent Classification:** Employs a pre-trained `Rasa NLU` model to identify the user's intent (e.g., `send_money`, `top_up`).
- **Web Interface:** A simple web UI to record voice commands and display the results.
- **Real-time Interaction:** Uses WebSockets for instant communication between the client and the server.
- **FastAPI Backend:** A robust and fast web framework for serving the application.

## Project Structure

```
.
├── actions/
│   └── actions.py
├── data/
│   ├── nlu.yml
│   ├── rules.yml
│   └── stories.yml
├── main.py
├── models/
│   └── nlu-20250804-135939-wise-deck.tar.gz
├── requirements.txt
├── server.py
└── templates/
    ├── index.html
    └── send_money.html
```

- **`main.py`**: Contains the core logic for loading the Rasa NLU model and processing text commands.
- **`server.py`**: The main FastAPI application that serves the web interface, handles WebSocket connections, and integrates the Whisper and Rasa components.
- **`data/`**: Contains the Rasa NLU training data.
- **`models/`**: Stores the trained Rasa NLU model and the downloaded Whisper model.
- **`templates/`**: HTML templates for the web interface.

## How it Works

1.  The user opens the web interface and starts recording their voice.
2.  The audio is streamed to the FastAPI backend via a WebSocket connection.
3.  The `server.py` script receives the audio chunks and uses the `whisper` model to transcribe them into text.
4.  The transcribed text is then passed to the `NLUProcessor` from `main.py`.
5.  The `NLUProcessor` uses the trained Rasa model to classify the intent of the text.
6.  The result, including the transcribed text and the classified intent, is sent back to the client and displayed on the web page.

## Getting Started

### Prerequisites

- Python 3.8+
- Pip

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/Rohanpudasaini/Chatbot.git
    cd Chatbot
    ```

2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

To start the FastAPI server, run the following command:

```bash
python server.py
```

The application will be available at `http://localhost:8000`.
