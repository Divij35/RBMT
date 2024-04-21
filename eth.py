from nltk.tokenize import word_tokenize
from Translations_rules import translation_rules

def translate(input_text, translation_rules):
    tokens = word_tokenize(input_text.lower())
    translated_text = ""
    for token in tokens:
        translated_token = translation_rules.get(token, token)
        translated_text += translated_token + " "
    return translated_text.strip()

english_text = input("Enter the English text: ")

hindi_text = translate(english_text, translation_rules)

print("Translated Hindi Text:", hindi_text)
