from googletrans import Translator

# Initialize the translator
translator = Translator()

# Dictionary mapping languages to their ISO codes
languages = {
    
    'hindi': 'hi',
    'kannada':'kn',
    'telugu': 'te',
    'or': 'odia',
    'bengali': 'bn',
    'tamil': 'ta',
    'gujarati': 'gu',
    'marathi': 'mr',
    'urdu': 'ur',
    'english': 'en',
    'french': 'fr',
    'malayalam': 'ml',
    'german': 'de',
    'italian': 'it',
    'portuguese': 'pt',
    'russian': 'ru',
    'spanish': 'es'
}

def translate_text(text, dest_language):
    translation = translator.translate(text, src='en', dest=dest_language)
    # Check if translation is successful before accessing .text attribute
    if translation:
        return translation.text
    else:
        return "Translation failed"  # Return an error message if translation fails

def translate_to_all_languages(text):
    translations = {}
    for language, code in languages.items():
        translated_text = translate_text(text, code)
        translations[language.capitalize()] = translated_text  # Capitalize language name for display
    return translations

def main():
    # Input text to translate
    text_to_translate = input("Enter text to translate: ")

    # Translate to all languages
    translations = translate_to_all_languages(text_to_translate)

    # Print original text
    print(f"\nOriginal text: {text_to_translate}\n")

    # Print translated text for each language
    for language, translation in translations.items():
        print(f"Translated text in {language}: {translation}")

if __name__ == "__main__":
    main()
