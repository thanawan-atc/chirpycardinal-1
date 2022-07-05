import random
import logging
from functools import cmp_to_key
from chirpy.core.util import infl
from chirpy.core.response_generator.response_type import add_response_types, ResponseType
from chirpy.response_generators.dinosaur.regex_templates.regex_templates import DINOSAUR, KEYWORD_DINOSAUR

from chirpy.core.entity_linker.entity_linker_simple import link_span_to_entity
from chirpy.core.entity_linker.entity_linker_classes import WikiEntity

from chirpy.response_generators.dinosaur.regex_templates.regex_templates import FavoriteDinosaurTemplate

import logging


import inflect
engine = inflect.engine()

logger = logging.getLogger('chirpylogger')

ADDITIONAL_RESPONSE_TYPES = ['DINOSAUR_KEYWORDS', 'FAVORITE_DINOSAUR']

ResponseType = add_response_types(ResponseType, ADDITIONAL_RESPONSE_TYPES)


def contains_dinosaur_keywords(rg, utterance):
    for word in KEYWORD_DINOSAUR:
        if word in utterance:
            return True
        return False

def get_dinosaur_entity(current_state) -> WikiEntity:
    return link_span_to_entity('dinosaur', current_state)

def extract_fav_dinosaur(rg):
    state, utterance, response_types = rg.get_state_utterance_response_types()
    slots = FavoriteDinosaurTemplate().execute(utterance)
    if slots is None: slots = {}
    place = slots.get('dinosaur', None)
    return place
