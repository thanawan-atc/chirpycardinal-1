import logging
from typing import Optional

from chirpy.core.response_generator import ResponseGenerator
from chirpy.core.response_priority import ResponsePriority, PromptType
from chirpy.core.response_generator_datatypes import emptyResult, ResponseGeneratorResult, PromptResult, emptyPrompt, \
    UpdateEntity, AnswerType
from chirpy.core.regex.regex_template import RegexTemplate
from chirpy.core.regex.response_lists import RESPONSE_TO_THATS, RESPONSE_TO_DIDNT_KNOW

from chirpy.response_generators.country.treelets.ask_favorite_country_treelet import AskFavoriteCountryTreelet
from chirpy.response_generators.country.treelets.ask_why_favorite_country_treelet import AskWhyFavoriteCountryTreelet
from chirpy.response_generators.country.regex_templates.word_lists import KEYWORD_COUNTRY
from chirpy.response_generators.country.state import State, ConditionalState

from chirpy.core.entity_linker.entity_groups import ENTITY_GROUPS_FOR_EXPECTED_TYPE
from chirpy.core.entity_linker.entity_linker_simple import link_span_to_entity

from chirpy.response_generators.country.country_helpers import *

logger = logging.getLogger('chirpylogger')

class CountryResponseGenerator(ResponseGenerator):
    name = 'COUNTRY'

    def __init__(self, state_manager) -> None:
        self.ask_favorite_country_treelet = AskFavoriteCountryTreelet(self)
        self.ask_why_favorite_country_treelet = AskWhyFavoriteCountryTreelet(self)

        treelets = {
            treelet.name: treelet for treelet in [self.ask_favorite_country_treelet, self.ask_why_favorite_country_treelet]
        }

        super().__init__(state_manager, treelets=treelets, intent_templates=[], can_give_prompts=True,
                         state_constructor=State,
                         conditional_state_constructor=ConditionalState,
                         trigger_words=["country"])


    def identify_response_types(self, utterance):
        response_types = super().identify_response_types(utterance)

        if is_country_keyword(self, utterance):
            response_types.add(ResponseType.COUNTRY_KEYWORD)

        return response_types


    def get_country_entity(self, string):
        return link_span_to_entity(string, self.state_manager.current_state,
            expected_type=ENTITY_GROUPS_FOR_EXPECTED_TYPE.country)




