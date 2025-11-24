This is a Python-based desktop application built using Tkinter, designed to provide a complete multilingual translation solution.
It supports text translation, audio translation, document translation (PDF, DOCX, PPTX), image OCR, speech recognition, and text-to-speech.

It is built on top of reliable libraries like googletrans, SpeechRecognition, gTTS, pydub, pdfplumber, python-pptx, and Tesseract OCR.

> Key Features
> Text Translation

Translate any input text into 25+ languages.

Supports long paragraphs and multi-line inputs.

Accurate and fast using googletrans.

> Audio Translation & Speech Recognition

Convert spoken audio from microphone into text using Google Speech Recognition.

Supports translation from microphone input to any target language.

Upload and transcribe audio files:

.mp3

.wav

.ogg

.flac

> Text-to-Speech (TTS)

Listen to translated output using Google Text-to-Speech (gTTS).

Clear playback using pygame.

Save audio output as:

.mp3

.wav

> Save Translations

Save translated text as:

.txt

.docx

Save spoken output as audio files.

📤 Document Translation (Advanced Feature)

(Newly Added)

This application now supports full document translation pipeline, including:

> PDF Translation

Extract text using pdfplumber.

Automatically detect document language.

Translate entire PDF text cleanly.

> DOCX Translation

Extract paragraphs and table content.

Maintain paragraph structure.

> PPTX Translation

Extract slide text using python-pptx.

Translate slide-by-slide content.

> Image OCR Translation

Convert images to text using Tesseract OCR.

Supports:

.png

.jpg

.jpeg

.bmp

.tif

.tiff

 Smart Features (New)
 Auto Language Detection

Detects the language of uploaded text, document, or OCR-extracted text.

Automatically sets the input language for accurate translation.

 Document Mode (Paragraph-wise Translation)

Translates documents paragraph by paragraph for:

Better accuracy

Preserved structure

More natural output

🛠️ Technologies Used
Backend / Core

googletrans – Language translation

SpeechRecognition – Speech-to-text

gTTS – Text-to-speech

pydub – Audio format handling

pythoncom – Windows COM initialization

pygame – Audio playback

Document Processing

python-docx – DOCX extraction & saving

pdfplumber – PDF text extraction

python-pptx – PPTX parsing

pytesseract – OCR for images

Pillow – Image processing

UI

Tkinter – Clean and responsive desktop interface

🌍 Supported Languages

Includes major languages like:

English

Hindi

Telugu

Tamil

Bengali

Marathi

Kannada

Malayalam

Gujarati

Urdu

French

German

Spanish

Japanese

Chinese

Korean

Russian

Arabic

Dutch

Turkish

Italian

Portuguese
