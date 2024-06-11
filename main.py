import numpy as np
import playsound
import pyaudio
import speech_recognition as sr
import wave

from ctypes import *
from faster_whisper import WhisperModel


def main():
    listen("computer") # forever listen for keyword
    record("audio/temp.mp3")

    transcription = transcribe("audio/temp.mp3")

    print(f"Transcription: {transcription}")


def listen(keyWord):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Please start speaking..\n')
        while True: 
            try:
                audio = r.listen(source)
                text = r.recognize_google(audio)
                print(text)
                if keyWord.lower() in text.lower():
                    return True
            except Exception as e:
                print(f"Error: {e}")


def record(file):
    playsound.playsound('audio/start.mp3', block=False)

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    THRESHOLD = 250
    WAVE_OUTPUT_FILENAME = file

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    print("start recording...")
    frames = []
    silent_time = 0
    
    while True:
        data = stream.read(CHUNK)
        frames.append(data)
        
        # Convert data to numpy array
        audio_data = np.frombuffer(data, dtype=np.int16)
        
        # Check the level of noise
        if np.abs(audio_data).mean() < THRESHOLD:
            silent_time += CHUNK / RATE  # Increase silent time
            if silent_time >= 3:  # If silent for 3 seconds, break the loop
                break
        else:
            silent_time = 0  # Reset silent time

    print("recording stopped")

    playsound.playsound('audio/stop.mp3', block=False)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    SAMPLE_SIZE = p.get_sample_size(FORMAT)
    p.terminate()

    # Save the recorded frames to a WAV file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(SAMPLE_SIZE)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def transcribe(file):
    model_size = "tiny.en"
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    print("Transcribing...")
    segments, _ = model.transcribe(file, beam_size=5)

    return " ".join([segment.text for segment in segments])


if __name__ == "__main__":
        main()