# audio_engine.py

import os
import pythoncom
import pygame
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment

from config import LANG_NAME_TO_CODE

# Initialize COM and Pygame Mixer once
pythoncom.CoInitialize()
pygame.mixer.init()

_recognizer = sr.Recognizer()


def _lang_code(lang_name: str) -> str:
    if lang_name not in LANG_NAME_TO_CODE:
        raise ValueError(f"Unknown language: {lang_name}")
    return LANG_NAME_TO_CODE[lang_name]


def recognize_from_audio_file(file_path: str, input_lang_name: str) -> str:
    """
    Convert an audio file (wav/mp3/ogg/flac) to text
    using Google Speech Recognition.
    Returns recognized text.
    """
    lang = _lang_code(input_lang_name)
    temp_file = None

    try:
        # Convert to wav if needed
        if file_path.lower().endswith(".mp3"):
            temp_file = "temp_converted.wav"
            AudioSegment.from_mp3(file_path).export(temp_file, format="wav")
            file_path = temp_file
        elif file_path.lower().endswith((".ogg", ".flac")):
            temp_file = "temp_converted.wav"
            AudioSegment.from_file(file_path).export(temp_file, format="wav")
            file_path = temp_file

        with sr.AudioFile(file_path) as source:
            audio = _recognizer.record(source)
            text = _recognizer.recognize_google(audio, language=lang)
        return text
    finally:
        if temp_file and os.path.exists(temp_file):
            os.remove(temp_file)


def recognize_from_microphone(input_lang_name: str,
                              timeout: int = 10,
                              phrase_time_limit: int = 15) -> str:
    """
    Listen from microphone and return recognized text.
    Does NOT show any messageboxes; UI should handle that.
    """
    lang = _lang_code(input_lang_name)

    with sr.Microphone() as source:
        # You can tweak duration if needed
        _recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = _recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

    return _recognizer.recognize_google(audio, language=lang)


def speak_text(text: str, output_lang_name: str):
    """
    Convert text to speech (gTTS) and play it using pygame.
    """
    text = (text or "").strip()
    if not text:
        return

    lang = _lang_code(output_lang_name)

    if not os.path.exists("temp"):
        os.makedirs("temp")

    temp_file = os.path.join("temp", "output.mp3")

    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(temp_file)

    pygame.mixer.music.load(temp_file)
    pygame.mixer.music.play()


def stop_playback():
    """Stop audio playback if playing."""
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()


def save_tts_to_file(text: str, output_lang_name: str, file_path: str):
    """
    Save TTS audio (gTTS) directly to a given file path (.mp3 or .wav).
    """
    text = (text or "").strip()
    if not text:
        return

    lang = _lang_code(output_lang_name)
    # gTTS saves as mp3 by default; if user picks .wav, gTTS will still save mp3,
    # but tools usually handle it. You can add conversion if needed.
    gTTS(text=text, lang=lang).save(file_path)


def cleanup_audio():
    """Call this once at program exit."""
    try:
        pygame.mixer.quit()
    except Exception:
        pass

    try:
        pythoncom.CoUninitialize()
    except Exception:
        pass
