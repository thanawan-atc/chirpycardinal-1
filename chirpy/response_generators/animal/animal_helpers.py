import random
import logging
from functools import cmp_to_key
from chirpy.core.util import infl
from chirpy.core.response_generator.response_type import add_response_types, ResponseType
from chirpy.response_generators.animal.regex_templates import FavoriteTypeTemplate
from chirpy.response_generators.animal.regex_templates import ANIMALS, CATEGORIES
import logging

import inflect
engine = inflect.engine()

logger = logging.getLogger('chirpylogger')

ADDITIONAL_RESPONSE_TYPES = ['RECOGNIZED_ANIMAL', 'UNKNOWN_ANIMAL', 'RECOGNIZED_UTTERANCE_TYPE']

ResponseType = add_response_types(ResponseType, ADDITIONAL_RESPONSE_TYPES)

def is_recognized_animal(rg, utterance):
    slots = FavoriteTypeTemplate().execute(utterance)
    return slots is not None and is_known_animal(slots['type'])

def is_unknown_animal(rg, utterance):
    slots = FavoriteTypeTemplate().execute(utterance)
    return slots is not None and not is_known_animal(slots['type'])

def is_known_animal(animal: str) -> bool:
    """Make sure to call this first, all of the following functions assume input is in FOODS"""
    logger.primary_info(str((animal.lower() in ANIMALS) or get_custom_question(animal)))
    return (animal.lower() in ANIMALS) or get_custom_question(animal)

def get_animal_data(animal):
    return ANIMALS[animal.lower()]

def is_subclassable(animal: str):
    return animal.lower() in CATEGORIES

def sample_from_type(animal):
    # logger.primary_info(food)
    # logger.primary_info(FOODS.items())
    animal = animal.lower()
    animals = [(ani, ani_data) for ani, ani_data in ANIMALS.items() if ani_data['type'] == animal]
    weights = [ani_data['views']**2 for ani, ani_data in animals]
    logger.primary_info(f"Sampling from: {[ani[0] for ani in animals]}, weights={weights}")
    ani_name, ani_data = random.choices(animals, weights=weights)[0]
    return ani_name # food_data['name']

def get_attribute(animal: str):
    if animal is None: return None, None
    animal = animal.lower()
    if animal not in ANIMALS: return None, None
    animal_data = get_animal_data(food)
    if 'ingredients' in animal_data:
        return 'ingredient', sample_ingredient(animal)
    elif 'texture' in animal_data:
        return 'texture', animal_data['texture']
    # elif 'origin' in food_data:
    #     return 'origin', food_data['origin']
    return None, None

def get_classes_of(ani_class: str) -> set:
    """Returns subtypes of a class of food"""
    ani_class = ani_class.lower()
    return ANIMALS[ani_class].get('types', [])

def get_class_of(subtype: str) -> str:
    """Returns class of a given food, empty string if none"""
    subtype = subtype.lower()
    for animal in ANIMALS:
        if subtype in ANIMALS[animal].get('types', []):
            return animal
    return ''

def get_associated_subtypes(subtype: str) -> set:
    """Returns other foods in the same class as set, empty set if none"""
    subtype = subtype.lower()
    for animal in ANIMALS:
        if subtype in ANIMALS[animal]['types']:
            return ANIMALS[animal]['types'] - set([subtype])
    return set()

INTRO_STATEMENTS = [
    "Ah yes, [FOOD] [copula] one of my favorite animals.",
]

def get_intro_acknowledgement(cur_food, is_plural):
    intro_statement = random.choice(INTRO_STATEMENTS)
    copula = infl('is', is_plural)
    return intro_statement.replace('[copula]', copula).replace('[FOOD]', cur_food)

CONCLUDING_STATEMENTS = ["Anyway, thanks for talking to me about {}."]

def get_concluding_statement(cur_food):
    return random.choice(CONCLUDING_STATEMENTS).format(cur_food)