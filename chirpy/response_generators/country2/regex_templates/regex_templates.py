from chirpy.core.regex.regex_template import RegexTemplate
from chirpy.response_generators.country2.regex_templates.word_lists import *
from chirpy.core.regex.util import OPTIONAL_TEXT_PRE, OPTIONAL_TEXT_MID, OPTIONAL_TEXT_POST, \
    OPTIONAL_TEXT_PRE_GREEDY, NONEMPTY_TEXT
from chirpy.core.regex.word_lists import CONTINUER


class FavoriteCountryTemplate(RegexTemplate):
    slots = {
        'yes_word': YES_WORDS,
        'no_word' : NO_WORDS,
        'watch_word': WATCH_WORDS,
        'type': TYPES,
        'continuer' : CONTINUER,
        'positive_adjective': POSITIVE_ADJECTIVES,
        'positive_verb': POSITIVE_VERBS,
        'positive_adverb': POSITIVE_ADVERBS,
        'keyword_country': KEYWORD_COUNTRY,
        'country': list(COUNTRY.keys())
    }
    templates = [
        "{country}",
        "my favorite {keyword_country} is {country}",
        "my favorite is {country}",
        "my favorite {keyword_country} of all time is {country}",
        "my favorite of all time is {country}",
        "my favorite {keyword_country} is probably {country}",
        "my favorite is probably {country}",
        "my favorite {keyword_country} of all time is probably {country}",
        "my favorite of all time is probably {country}",
        "i {positive_verb} {country}",
        OPTIONAL_TEXT_PRE + "{positive_verb}" + OPTIONAL_TEXT_MID + "{country}",
        "i {positive_adverb} {positive_verb} {country}",
        "i think {country} is {positive_adjective}",
        "i follow {country}",
        "{continuer} my favorite {keyword_country} is {country}",
        "{continuer} my favorite is {country}",
        "{continuer} i {positive_verb} {country}",
        "{continuer} i {positive_adverb} {positive_verb} {country}",
        "{continuer} i think {country} is {positive_adjective}",
        "probably {country}",
        "{continuer} probably {country}",
        "i'd have to say {country}",
        "i guess i'd have to say {country}",
        "maybe {country}",
        "i guess {country}",
        "i think {country}"
    ]

    positive_examples = []
    negative_examples = []

class FavoritePlaceTemplate(RegexTemplate):
    slots = {
        'yes_word': YES_WORDS,
        'no_word' : NO_WORDS,
        'watch_word': WATCH_WORDS,
        'type': TYPES,
        'continuer' : CONTINUER,
        'positive_adjective': POSITIVE_ADJECTIVES,
        'positive_verb': POSITIVE_VERBS,
        'positive_adverb': POSITIVE_ADVERBS,
        'keyword_place': KEYWORD_PLACE,
        'famous_place': PLACE
    }
    templates = [
        "{famous_place}",
        "my favorite {keyword_place} is {famous_place}",
        "my favorite is {famous_place}",
        "my favorite {keyword_place} of all time is {famous_place}",
        "my favorite of all time is {famous_place}",
        "my favorite {keyword_place} is probably {famous_place}",
        "my favorite is probably {famous_place}",
        "my favorite {keyword_place} of all time is probably {famous_place}",
        "my favorite of all time is probably {famous_place}",
        "i {positive_verb} {famous_place}",
        OPTIONAL_TEXT_PRE + "{positive_verb}" + OPTIONAL_TEXT_MID + "{famous_place}",
        "i {positive_adverb} {positive_verb} {famous_place}",
        "i think {famous_place} is {positive_adjective}",
        "i follow {famous_place}",
        "{continuer} my favorite {keyword_place} is {famous_place}",
        "{continuer} my favorite is {famous_place}",
        "{continuer} i {positive_verb} {famous_place}",
        "{continuer} i {positive_adverb} {positive_verb} {famous_place}",
        "{continuer} i think {famous_place} is {positive_adjective}",
        "probably {famous_place}",
        "{continuer} probably {famous_place}",
        "i'd have to say {famous_place}",
        "i guess i'd have to say {famous_place}",
        "maybe {famous_place}",
        "i guess {famous_place}",
        "i think {famous_place}"
    ]

    positive_examples = []
    negative_examples = []