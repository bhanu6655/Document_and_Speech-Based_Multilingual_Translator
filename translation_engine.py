# translation_engine.py

from googletrans import Translator
from config import LANG_NAME_TO_CODE

# Single Translator instance reused
_translator = Translator()

# Same limit you used earlier
MAX_CHUNK_SIZE = 5000


def translate_text(text: str, target_lang_name: str) -> str:
    """
    Translate a long text into the target language.
    - text: input text to translate
    - target_lang_name: e.g. "Hindi", "French"
    Returns the translated string (or empty string if input is empty).
    """
    text = (text or "").strip()
    if not text:
        return ""

    if target_lang_name not in LANG_NAME_TO_CODE:
        raise ValueError(f"Unknown language: {target_lang_name}")

    lang_code = LANG_NAME_TO_CODE[target_lang_name]

    # Split into chunks to avoid googletrans length issues
    chunks = [text[i:i + MAX_CHUNK_SIZE] for i in range(0, len(text), MAX_CHUNK_SIZE)]

    translated_chunks = []
    for chunk in chunks:
        result = _translator.translate(chunk, dest=lang_code)
        translated_chunks.append(result.text)

    return " ".join(translated_chunks)
