# config.py

# Language display names (same as your current lt list)
LANG_NAMES = [
    "English", "Hindi", "Tamil", "Gujarati", "Marathi", "Telugu", "Bengali",
    "Kannada", "Malayalam", "French", "Spanish", "German", "Chinese",
    "Japanese", "Russian", "Italian", "Portuguese", "Dutch", "Turkish",
    "Arabic", "Korean", "Swedish", "Norwegian", "Danish", "Polish", "Czech", "Urdu"
]

# Corresponding language codes (same as your current code list)
LANG_CODES = [
    "en", "hi", "ta", "gu", "mr", "te", "bn", "kn", "ml", "fr", "es", "de",
    "zh-CN", "ja", "ru", "it", "pt", "nl", "tr", "ar", "ko", "sv", "no", "da",
    "pl", "cs", "ur"
]

# Helpful mappings
LANG_NAME_TO_CODE = dict(zip(LANG_NAMES, LANG_CODES))
LANG_CODE_TO_NAME = dict(zip(LANG_CODES, LANG_NAMES))
