from chirpy.core.regex.regex_template import RegexTemplate
from chirpy.response_generators.color2.regex_templates.word_lists import *
from chirpy.core.regex.util import OPTIONAL_TEXT_PRE, OPTIONAL_TEXT_MID, OPTIONAL_TEXT_POST, \
    OPTIONAL_TEXT_PRE_GREEDY, NONEMPTY_TEXT
from chirpy.core.regex.word_lists import CONTINUER


class FavoriteColorTemplate(RegexTemplate):
    slots = {
        'yes_word': YES_WORDS,
        'no_word' : NO_WORDS,
        'watch_word': WATCH_WORDS,
        'type': TYPES,
        'continuer' : CONTINUER,
        'positive_adjective': POSITIVE_ADJECTIVES,
        'positive_verb': POSITIVE_VERBS,
        'positive_adverb': POSITIVE_ADVERBS,
        'keyword_color': KEYWORD_COLOR,
        'color': COLORS
    }
    templates = [
        "{color}",
        "my favorite {keyword_color} is {color}",
        "my favorite is {color}",
        "my favorite {keyword_color} of all time is {color}",
        "my favorite of all time is {color}",
        "my favorite {keyword_color} is probably {color}",
        "my favorite is probably {color}",
        "my favorite {keyword_color} of all time is probably {color}",
        "my favorite of all time is probably {color}",
        "i {positive_verb} {color}",
        OPTIONAL_TEXT_PRE + "{positive_verb}" + OPTIONAL_TEXT_MID + "{color}",
        "i {positive_adverb} {positive_verb} {color}",
        "i think {color} is {positive_adjective}",
        "i follow {color}",
        "{continuer} my favorite {keyword_color} is {color}",
        "{continuer} my favorite is {color}",
        "{continuer} i {positive_verb} {color}",
        "{continuer} i {positive_adverb} {positive_verb} {color}",
        "{continuer} i think {color} is {positive_adjective}",
        "probably {color}",
        "{continuer} probably {color}",
        "i'd have to say {color}",
        "i guess i'd have to say {color}",
        "maybe {color}",
        "i guess {color}",
        "i think {color}"
    ]

    positive_examples = []
    negative_examples = []