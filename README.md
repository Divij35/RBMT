# Rule Based Machine Translation
This is a simple rule-based machine translation system implemented in Python. It translates sentences from English to Hindi based on predefined translation rules and a lexicon.  : Rule-based machine translation (RBMT) is a traditional approach to machine translation that relies on a set of linguistic rules and patterns to translate text from one language to another. In RBMT, translations are generated based on explicit rules that govern the transformation of input text from the source language into the target language.

## NOTE
eth.py and rule_based.py are two different files.  
1. eth.py uses nltk
1. While rule_based.py is implemented from scratch  

### Overview
The system consists of the following components:

1. RuleBasedTranslator Class: This class contains methods for translating sentences and texts. It initializes with translation rules and a lexicon.
1. Translation Rules: Rules define translation patterns, such as 'subject-verb-object' or 'object-verb-subject'. These rules guide the translation process.
1. Lexicon: The lexicon contains mappings between words in English and Hindi. It provides translations for individual words or word combinations.

### Prerequisite 
1. python
1. nltk

### Usage 
> pip install nltk

`python rule_based.py` for the original version
`python eth.py` for running the nltk version 
 
To change or add translation rules check the `Translation_rules.py` file.  
The left side words are the english words while the right side words are the hindi words.

### Contributing
Contributions to improve the translation rules or expand the lexicon are welcome. Feel free to fork the repository, make improvements, and submit pull requests. For further details - see the [CONTRIBUTING.md](CONTRIBUTING.md) 😄

### License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

