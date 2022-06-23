from chirpy.core.regex.regex_template import RegexTemplate
from chirpy.response_generators.color.regex_templates.word_lists import *
from chirpy.core.regex.util import OPTIONAL_TEXT_PRE, OPTIONAL_TEXT_MID, OPTIONAL_TEXT_POST, \
    OPTIONAL_TEXT_PRE_GREEDY, NONEMPTY_TEXT
from chirpy.core.regex.word_lists import CONTINUER


class FavoriteTypeTemplate(RegexTemplate):
    slots = {
        'yes_word': YES_WORDS,
        'no_word' : NO_WORDS,
        'watch_word': WATCH_WORDS,
        'type': TYPES,
        'continuer' : CONTINUER,
        'positive_adjective': POSITIVE_ADJECTIVES,
        'positive_verb': POSITIVE_VERBS,
        'positive_adverb': POSITIVE_ADVERBS,
        'country': list(COUNTRY.keys())
    }
    templates = [
        "my favorite {country} is {type}",
        "my favorite is {type}",
        "my favorite {country} of all time is {type}",
        "my favorite of all time is {type}",
        "my favorite {country} is probably {type}",
        "my favorite is probably {type}",
        "my favorite {country} of all time is probably {type}",
        "my favorite of all time is probably {type}",
        "i {positive_verb} {type}",
        "i {positive_adverb} {positive_verb} {type}",
        "i think {type} is {positive_adjective}",
        "i follow {type}",
        "{continuer} my favorite {country} is {type}",
        "{continuer} my favorite is {type}",
        "{continuer} i {positive_verb} {type}",
        "{continuer} i {positive_adverb} {positive_verb} {type}",
        "{continuer} i think {type} is {positive_adjective}",
        "probably {type}",
        "{continuer} probably {type}",
        "i'd have to say {type}",
        "i guess i'd have to say {type}",
        "maybe {type}",
        "i guess {type}",
        "i think {type}",
        "{continuer} i'd have to say {type}",
        "{continuer} i guess i'd have to say {type}",
        "{continuer} maybe {type}",
        "{continuer} i guess {type}",
        "{continuer} i think {type}",
        "{yes_word} i {watch_word} {type}",
        "{yes_word} i recently {watch_word} {type}",
        "{yes_word} lately i {watch_word} {type}",
        "{yes_word} {type}",
        "{continuer} {type}",
        "{continuer} {yes_word} {type}",
        "{type}"
    ]

    positive_examples = []
    negative_examples = []