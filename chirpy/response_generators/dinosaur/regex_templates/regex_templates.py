from chirpy.core.regex.regex_template import RegexTemplate
from chirpy.response_generators.dinosaur.regex_templates.word_lists import *
from chirpy.core.regex.util import OPTIONAL_TEXT_PRE, OPTIONAL_TEXT_MID, OPTIONAL_TEXT_POST, \
    OPTIONAL_TEXT_PRE_GREEDY, NONEMPTY_TEXT
from chirpy.core.regex.word_lists import CONTINUER


class FavoriteDinosaurTemplate(RegexTemplate):
    slots = {
        'yes_word': YES_WORDS,
        'no_word' : NO_WORDS,
        'watch_word': WATCH_WORDS,
        'type': TYPES,
        'continuer' : CONTINUER,
        'positive_adjective': POSITIVE_ADJECTIVES,
        'positive_verb': POSITIVE_VERBS,
        'positive_adverb': POSITIVE_ADVERBS,
        'keyword_dinosaur': KEYWORD_DINOSAUR,
        'dinosaur': list(DINOSAUR.keys())
    }
    templates = [
        "{dinosaur}",
        "my favorite {keyword_dinosaur} is {dinosaur}",
        "my favorite is {dinosaur}",
        "my favorite {keyword_dinosaur} of all time is {dinosaur}",
        "my favorite of all time is {dinosaur}",
        "my favorite {keyword_dinosaur} is probably {dinosaur}",
        "my favorite is probably {dinosaur}",
        "my favorite {keyword_dinosaur} of all time is probably {dinosaur}",
        "my favorite of all time is probably {dinosaur}",
        "i {positive_verb} {dinosaur}",
        OPTIONAL_TEXT_PRE + "{positive_verb}" + OPTIONAL_TEXT_MID + "{dinosaur}",
        "i {positive_adverb} {positive_verb} {dinosaury}",
        "i think {dinosaur} is {positive_adjective}",
        "i follow {dinosaur}",
        "{continuer} my favorite {keyword_dinosaur} is {dinosaur}",
        "{continuer} my favorite is {dinosaur}",
        "{continuer} i {positive_verb} {dinosaur}",
        "{continuer} i {positive_adverb} {positive_verb} {dinosaur}",
        "{continuer} i think {dinosaur} is {positive_adjective}",
        "probably {dinosaur}",
        "{continuer} probably {dinosaur}",
        "i'd have to say {dinosaur}",
        "i guess i'd have to say {dinosaur}",
        "maybe {dinosaur}",
        "i guess {dinosaur}",
        "i think {dinosaur}"
    ]

    positive_examples = []
    negative_examples = []
