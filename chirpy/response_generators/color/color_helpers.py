import random
import logging
from functools import cmp_to_key
from chirpy.core.util import infl
from chirpy.core.response_generator.response_type import add_response_types, ResponseType
from chirpy.response_generators.color.regex_templates.regex_templates import FavoriteTypeTemplate
from chirpy.response_generators.color.regex_templates.regex_templates import COLORS
import logging

import inflect
engine = inflect.engine()

logger = logging.getLogger('chirpylogger')

ADDITIONAL_RESPONSE_TYPES = ['RECOGNIZED_COLOR','RECOGNIZED_UTTERANCE_TYPE']

ResponseType = add_response_types(ResponseType, ADDITIONAL_RESPONSE_TYPES)

def is_recognized_color(rg, utterance):
    slots = FavoriteTypeTemplate().execute(utterance)
    return slots is not None and is_known_color(slots['type'])

def is_known_color(color: str) -> bool:
    """Make sure to call this first, all of the following functions assume input is in FOODS"""
    logger.primary_info(str((color.lower() in COLORS)))
    return color.lower() in COLORS
