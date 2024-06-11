# Voice Activation and Transcription System

This program is designed to continuously listen for a specific keyword, record audio upon detecting the keyword, and then transcribe the recorded audio into text using the Whisper Model.

## Features

1. **Keyword Detection**: Continuously listens for a specified keyword.
2. **Audio Recording**: Records audio upon detecting the keyword.
3. **Transcription**: Transcribes the recorded audio into text.

## Dependencies

- `numpy`
- `playsound`
- `pyaudio`
- `speech_recognition`
- `wave`
- `ctypes`
- `faster_whisper`

## Installation

1. **Install required Python packages**:
    ```bash
    pip install numpy playsound pyaudio SpeechRecognition wave faster-whisper
    ```
    ```bash
    pip install -r requirements.txt
    ```

2. **Install additional system dependencies**:
    - For `pyaudio`, you may need to install portaudio:
      ```bash
      sudo apt-get install portaudio19-dev  # For Debian-based systems
      brew install portaudio               # For macOS
      ```

## Usage

1. **Prepare Audio Cues**:
    - Ensure you have `start.mp3` and `stop.mp3` files in the `audio` directory to signal the start and stop of recording.

2. **Run the Program**:
    ```bash
    python main.py
    ```

3. **Specify the Keyword**:
    - The keyword to listen for is hardcoded in the `main()` function (`"computer"` by default).

## Functionality

### `main()`

The main function orchestrates the workflow:

1. Calls `listen("computer")` to wait for the keyword.
2. Once the keyword is detected, it records audio to `audio/temp.mp3`.
3. Transcribes the recorded audio and prints the transcription.

### `listen(keyWord)`

Continuously listens through the microphone until the specified keyword is detected.

- **Parameters**:
  - `keyWord` (str): The keyword to listen for.
- **Returns**:
  - `True` when the keyword is detected.

### `record(file)`

Records audio until 3 seconds of silence is detected.

- **Parameters**:
  - `file` (str): The file path to save the recorded audio.

### `transcribe(file)`

Transcribes the given audio file using the Whisper Model.

- **Parameters**:
  - `file` (str): The file path of the audio to be transcribed.
- **Returns**:
  - The transcription text.

## Notes

- Ensure your microphone is working properly and set up as the default input device.
- The recording will stop automatically after 3 seconds of silence.

## Troubleshooting

- **No audio detected**:
  - Ensure your microphone is properly connected and set as the default recording device.
- **Keyword not detected**:
  - Speak clearly and ensure the keyword is included in the spoken sentence.
- **Dependencies not found**:
  - Reinstall the required packages using the installation steps provided.

For further assistance, refer to the documentation of the respective libraries used.