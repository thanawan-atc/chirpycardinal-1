import random
import logging
from functools import cmp_to_key
from chirpy.core.util import infl
from chirpy.core.response_generator.response_type import add_response_types, ResponseType
from chirpy.response_generators.country2.regex_templates.regex_templates import FavoriteCountryTemplate
from chirpy.response_generators.country2.regex_templates.regex_templates import COUNTRY, KEYWORD_COUNTRY, KEYWORD_FOOD

from chirpy.core.entity_linker.entity_linker_simple import link_span_to_entity
from chirpy.core.entity_linker.entity_linker_classes import WikiEntity

from chirpy.response_generators.country2.regex_templates.regex_templates import FavoritePlaceTemplate

import logging


import inflect
engine = inflect.engine()

logger = logging.getLogger('chirpylogger')

ADDITIONAL_RESPONSE_TYPES = ['COUNTRY_KEYWORDS', 'FAVORITE_COUNTRY', 'FOOD_KEYWORDS',
                             'COUNTRY', 'ECONOMY', 'GEOGRAPHY', 'LANGUAGE', 'CUISINE']

ResponseType = add_response_types(ResponseType, ADDITIONAL_RESPONSE_TYPES)


def contains_country_keywords(rg, utterance):
    for word in KEYWORD_COUNTRY:
        if word in utterance:
            return True
        return False

def contains_food_keywords(rg, utterance):
    for word in KEYWORD_FOOD:
        if word in utterance:
            return True
        return False

def contains_specific_country(rg, utterance):
    for word in COUNTRY:
        if word in utterance:
            return True
        return False


def contains_geography(rg, utterance):
    if "geography" in utterance:
        return True
    return False

def contains_economy(rg, utterance):
    if "economy" in utterance:
        return True
    return False

def contains_language(rg, utterance):
    if "language" in utterance:
        return True
    return False


def contains_cuisine(rg, utterance):
    if "cuisine" in utterance:
        return True
    return False

def get_country_entity(current_state) -> WikiEntity:
    """Returns the WikiEntity for 'Country'"""
    return link_span_to_entity('country', current_state)

def extract_place(rg):
    state, utterance, response_types = rg.get_state_utterance_response_types()
    slots = FavoritePlaceTemplate().execute(utterance)
    if slots is None: slots = {}
    place = slots.get('famous_place', None)
    return place

def extract_country(rg):
    state, utterance, response_types = rg.get_state_utterance_response_types()
    slots = FavoriteCountryTemplate().execute(utterance)
    if slots is None: slots = {}
    country = slots.get('country', None)
    return country