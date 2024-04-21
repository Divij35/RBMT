from Translations_rules import translation_rules

class RuleBasedTranslator:
    def __init__(self, rules, lexicon):
        self.rules = rules
        self.lexicon = lexicon
    
    def translate_sentence(self, sentence, source_lang, target_lang):
        translated_tokens = []
        tokens = sentence.split()
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token in self.lexicon.get(source_lang, {}):
                translations = self.lexicon[source_lang].get(token, {})
                translation = translations.get(target_lang, token)
                next_token = tokens[i + 1] if i + 1 < len(tokens) else None
                if next_token is not None and f"{token} {next_token}" in self.lexicon.get(source_lang, {}):
                    combined_token = f"{token} {next_token}"
                    combined_translation = self.lexicon[source_lang].get(combined_token, {}).get(target_lang, combined_token)
                    translated_tokens.append(combined_translation)
                    i += 1
                else:
                    translated_tokens.append(translation)
            else:
                translated_tokens.append(token)
            i += 1
        
        return ' '.join(translated_tokens)
    
    def translate(self, text, source_lang, target_lang):
        sentences = text.split('.')
        translated_sentences = []
        for sentence in sentences:
            translated_sentence = self.translate_sentence(sentence.strip(), source_lang, target_lang)
            translated_sentences.append(translated_sentence)
        return '. '.join(translated_sentences)

rules = {
    'en': {
        'subject-verb-object': ['SVO'],
        'object-verb-subject': ['OVS']
    }
}

lexicon = {
    'en': {key: {'hi': value} for key, value in translation_rules.items()},
    'hi': {value: {'en': key} for key, value in translation_rules.items()}
}

translator = RuleBasedTranslator(rules, lexicon)

english_sentence = input("Enter a sentence in English: ").lower()

hindi_translation = translator.translate(english_sentence, 'en', 'hi')

print("Hindi Translation:", hindi_translation)
