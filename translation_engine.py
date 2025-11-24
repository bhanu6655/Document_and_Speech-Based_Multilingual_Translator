# translation_engine.py

from typing import List, Tuple

from googletrans import Translator
from config import LANG_NAME_TO_CODE, LANG_CODE_TO_NAME

# Single Translator instance reused
_translator = Translator()

MAX_CHUNK_SIZE = 5000


def translate_text(text: str, target_lang_name: str) -> str:
    """
    Translate a long text into the target language.
    """
    text = (text or "").strip()
    if not text:
        return ""

    lang_code = _lang_code_from_name(target_lang_name)

    chunks = [text[i:i + MAX_CHUNK_SIZE] for i in range(0, len(text), MAX_CHUNK_SIZE)]

    translated_chunks = []
    for chunk in chunks:
        result = _translator.translate(chunk, dest=lang_code)
        translated_chunks.append(result.text)

    return " ".join(translated_chunks)


def detect_language(text: str) -> Tuple[str, str]:
    """
    Detect the language of the given text.
    Returns (lang_code, lang_name_or_code_if_unknown).
    """
    text = (text or "").strip()
    if not text:
        return "", ""

    detection = _translator.detect(text)
    code = detection.lang  # e.g. 'en', 'hi'
    # Map to friendly name if known
    name = LANG_CODE_TO_NAME.get(code, code)
    return code, name


def translate_paragraphs(text: str, target_lang_name: str) -> str:
    """
    Split text into paragraphs and translate each paragraph separately.
    This is useful for documents to maintain structure better.
    """
    text = (text or "").strip()
    if not text:
        return ""

    paragraphs = _split_paragraphs(text)
    lang_code = _lang_code_from_name(target_lang_name)

    translated_paragraphs: List[str] = []
    for para in paragraphs:
        if not para.strip():
            translated_paragraphs.append("")  # keep blank lines
            continue
        result = _translator.translate(para, dest=lang_code)
        translated_paragraphs.append(result.text)

    # Join with double newlines to preserve paragraph breaks
    return "\n\n".join(translated_paragraphs)


# === Helpers ===

def _lang_code_from_name(lang_name: str) -> str:
    if lang_name not in LANG_NAME_TO_CODE:
        raise ValueError(f"Unknown language: {lang_name}")
    return LANG_NAME_TO_CODE[lang_name]


def _split_paragraphs(text: str) -> List[str]:
    """
    Split by double newlines first; if not present, fallback to single newline.
    """
    if "\n\n" in text:
        parts = text.split("\n\n")
    else:
        parts = text.splitlines()

    # Normalize whitespace
    return [p.strip() for p in parts]
