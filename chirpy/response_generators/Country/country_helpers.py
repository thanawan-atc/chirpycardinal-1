import random
import logging
from functools import cmp_to_key
from chirpy.core.util import infl
from chirpy.core.response_generator.response_type import add_response_types, ResponseType
from chirpy.response_generators.color.regex_templates.regex_templates import FavoriteTypeTemplate

from chirpy.response_generators.country.regex_templates.word_lists import KEYWORD_COUNTRY


import logging
import re

import inflect
engine = inflect.engine()

logger = logging.getLogger('chirpylogger')

ADDITIONAL_RESPONSE_TYPES = ['COUNTRY_KEYWORD']

ResponseType = add_response_types(ResponseType, ADDITIONAL_RESPONSE_TYPES)

def found_phrase(phrase, utterance):
    return re.search(f'(\A| ){phrase}(\Z| )', utterance) is not None

def is_country_keyword(rg, utterance):
    return any(found_phrase(i, utterance) for i in KEYWORD_COUNTRY)


