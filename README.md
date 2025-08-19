# Voice Playground AI - Updated Version

A FastAPI-based voice conversion application that uses ElevenLabs API to convert speech from one voice to another. This is a complete refactoring of the original React-based voice playground into a robust voice conversion service.

## 🚀 Features

- **Speech-to-Speech Conversion**: Convert audio files using different AI voices
- **Secure File Handling**: Safe upload and processing of audio files
- **Real-time Feedback**: Loading indicators and error handling
- **Voice Caching**: Efficient voice list management
- **Responsive Design**: Works on desktop and mobile devices
- **Error Handling**: Comprehensive error management and user feedback

## 🏗️ Project Structure

```
voiceplaygroundai_updated/
├── .env.example              # Environment variables template
├── core/
│   └── config.py            # Configuration management
├── main.py                  # Application entry point
├── requirements.txt         # Python dependencies
├── routers/
│   └── voice.py            # Voice conversion API routes
├── static/
│   ├── audio/              # Generated audio files
│   │   └── .gitkeep
│   ├── css/
│   │   └── style.css       # Styling
│   └── js/
│       └── script.js       # Frontend JavaScript
└── templates/
    └── index.html          # Main HTML template
```

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8+
- ElevenLabs API key

### Installation

1. **Clone or extract the project**
   ```bash
   cd voiceplaygroundai_updated
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your ElevenLabs API key
   ```

4. **Run the application**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Open your browser**
   Navigate to `http://localhost:8000`

## 🔧 Configuration

Create a `.env` file in the project root:

```env
ELEVENLABS_API_KEY=your_actual_api_key_here
```

## 📝 API Endpoints

### GET /
- Returns the main HTML interface
- Displays available voices from ElevenLabs

### POST /convert
- Accepts audio file upload and voice selection
- Returns converted audio file
- Handles errors gracefully

## 🔒 Security Features

- **File Type Validation**: Only accepts audio files
- **Secure File Handling**: Uses temporary files to prevent path traversal
- **Random Filenames**: Generated output files have secure, random names
- **Error Handling**: Comprehensive error management without exposing internals

## 🎯 Key Improvements

### From Original Version

1. **Correct API Usage**: Now uses Speech-to-Speech instead of Text-to-Speech
2. **Security**: Prevents path traversal attacks and validates file types
3. **Performance**: Caches voice list on startup instead of every request
4. **User Experience**: Real-time feedback and error handling
5. **Architecture**: Clean separation of concerns with proper project structure

### Technical Fixes

- Fixed core logic bug (was using TTS instead of STS)
- Added comprehensive error handling
- Implemented secure file upload handling
- Added loading indicators and status messages
- Improved project structure and maintainability

## 🚀 Deployment

### Local Development
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 🔍 Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your ElevenLabs API key is correctly set in `.env`
2. **File Upload Issues**: Check that you're uploading valid audio files
3. **Voice Loading**: If voices don't load, check API key and internet connection

### Error Messages

- **"Invalid file type"**: Upload an audio file (MP3, WAV, etc.)
- **"ElevenLabs API Error"**: Check your API key and account status
- **"Could not load voices"**: Verify API key and internet connectivity

## 📋 Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI
- **ElevenLabs**: Official ElevenLabs Python SDK
- **Pydantic Settings**: Configuration management
- **Jinja2**: Template engine for HTML rendering
- **Python Multipart**: File upload handling

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- ElevenLabs for the voice conversion API
- FastAPI for the excellent web framework
- Original voice playground concept for inspiration

