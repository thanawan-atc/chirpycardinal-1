import logging
from chirpy.core.regex.regex_template import RegexTemplate
from chirpy.core.regex.util import OPTIONAL_TEXT, NONEMPTY_TEXT, OPTIONAL_TEXT_PRE, OPTIONAL_TEXT_POST, \
    OPTIONAL_TEXT_MID
from chirpy.core.response_generator_datatypes import PromptType, ResponseGeneratorResult, PromptResult, emptyResult, \
    AnswerType
from chirpy.core.response_priority import ResponsePriority, PromptType
from chirpy.core.entity_linker.entity_groups import ENTITY_GROUPS_FOR_EXPECTED_TYPE
from chirpy.core.response_generator import Treelet
from chirpy.response_generators.country2.country_helpers import *
from chirpy.response_generators.country2.state import State, ConditionalState

from chirpy.core.entity_linker.entity_groups import EntityGroupsForExpectedType

import inflect

engine = inflect.engine()

logger = logging.getLogger('chirpylogger')

COMPLIMENT = ["fabulous", "remarkable!", "fantastic", "incredible"]


class AskAspectsTreelet(Treelet):
    name = "ask_aspects_treelet"

    def get_prompt(self, conditional_state=None):
        state, utterance, response_types = self.get_state_utterance_response_types()


        return PromptResult(text="What aspect would you like to know about? Geography, economy, language, or cuisine?",
                            prompt_type=PromptType.CURRENT_TOPIC,
                            cur_entity=self.rg.get_current_entity(),
                            state=state, conditional_state=conditional_state)

    def generate_aspect_response(self, cur_country, response_types):

        return "TODO3"

    def get_response(self, priority=ResponsePriority.STRONG_CONTINUE):
        state, utterance, response_types = self.get_state_utterance_response_types()

        cur_country = State.cur_country

        response = self.generate_aspect_response(cur_country, response_types)


        return ResponseGeneratorResult(
            text=response,
            priority=ResponsePriority.STRONG_CONTINUE,
            needs_prompt=True, state=state,
            cur_entity=self.rg.get_current_entity(),
            conditional_state=self.rg.ConditionalState(
                prev_treelet_str=self.name,
                next_treelet_str="transition")
        )




