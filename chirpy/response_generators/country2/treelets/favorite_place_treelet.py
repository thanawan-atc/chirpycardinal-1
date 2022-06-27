import logging
from chirpy.core.regex.regex_template import RegexTemplate
from chirpy.core.regex.util import OPTIONAL_TEXT, NONEMPTY_TEXT, OPTIONAL_TEXT_PRE, OPTIONAL_TEXT_POST, \
    OPTIONAL_TEXT_MID
import random
from chirpy.core.response_generator_datatypes import PromptType, ResponseGeneratorResult, PromptResult, emptyResult, AnswerType
from chirpy.core.response_priority import ResponsePriority, PromptType
from chirpy.core.entity_linker.entity_groups import ENTITY_GROUPS_FOR_EXPECTED_TYPE
from chirpy.core.response_generator import Treelet
from chirpy.response_generators.country2.country_helpers import *
from chirpy.response_generators.country2.state import State, ConditionalState

from chirpy.response_generators.country2.regex_templates.word_lists import PLACE, COUNTRY

from chirpy.core.entity_linker.entity_groups import EntityGroupsForExpectedType

import inflect
engine = inflect.engine()

logger = logging.getLogger('chirpylogger')


class FavoritePlaceTreelet(Treelet):
    name = "favorite_place_treelet"

    def get_prompt(self, conditional_state=None):
        state, utterance, response_types = self.get_state_utterance_response_types()

        return PromptResult(text="Is there any specific place you want to visit?",
                            prompt_type=PromptType.CURRENT_TOPIC,
                            cur_entity=self.rg.get_current_entity(),
                            state=state, conditional_state=conditional_state,
                            )

    def get_response(self, priority=ResponsePriority.STRONG_CONTINUE):
        state, utterance, response_types = self.get_state_utterance_response_types()

        if ResponseType.NO in response_types:


            return ResponseGeneratorResult(
                text="No worries ... ",
                priority=ResponsePriority.STRONG_CONTINUE,
                needs_prompt=False, state=state,
                cur_entity=self.rg.get_current_entity(),
                conditional_state=self.rg.ConditionalState(
                    prev_treelet_str=self.name,
                    prompt_treelet=self.rg.doubt_about_favorite_country_treelet.name
                )
            )

        else:
            cur_place = self.rg.get_current_entity()

            is_plural = cur_place.is_plural
            copula = infl('are', is_plural)
            pronoun = infl('they', is_plural)

            neural_response = self.rg.get_neural_response(
                prefix=f"{cur_place.talkable_name} {copula} a great choice! I especially love how {pronoun}")
            suffix = " I hope I have a chance to go there as well"

            return ResponseGeneratorResult(
                text=neural_response+suffix,
                priority=ResponsePriority.STRONG_CONTINUE,
                needs_prompt=True, state=state,
                cur_entity=self.rg.state_manager.current_state.entity_tracker.cur_entity,
                conditional_state=self.rg.ConditionalState(
                    prev_treelet_str=self.name,
                    next_treelet_str="transition",
                    cur_place=cur_place)
        )
