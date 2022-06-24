import random
import logging
from functools import cmp_to_key
from chirpy.core.util import infl
from chirpy.core.response_generator.response_type import add_response_types, ResponseType
from chirpy.response_generators.color2.regex_templates.regex_templates import FavoriteColorTemplate
from chirpy.response_generators.color2.regex_templates.regex_templates import COLORS

from chirpy.core.entity_linker.entity_linker_simple import link_span_to_entity
from chirpy.core.entity_linker.entity_linker_classes import WikiEntity

import logging

import inflect
engine = inflect.engine()

logger = logging.getLogger('chirpylogger')

ADDITIONAL_RESPONSE_TYPES = ['COLOR_KEYWORDS', 'FAVORITE_COLOR']

ResponseType = add_response_types(ResponseType, ADDITIONAL_RESPONSE_TYPES)


def contains_color_keywords(rg, utterance):
    if "color" in utterance:
        return True
    return False

def get_color_entity(current_state) -> WikiEntity:
    """Returns the WikiEntity for 'Color'"""
    return link_span_to_entity('color', current_state)

def favorite_color_detected(rg, utterance):
    return FavoriteColorTemplate().execute(utterance) is not None