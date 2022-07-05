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



class NextCountrySuggestionTreelet(Treelet):
    name = "next_country_suggestion_treelet"


    def get_response(self, priority=ResponsePriority.STRONG_CONTINUE):
        state, utterance, response_types = self.get_state_utterance_response_types()

        if ResponseType.NO in response_types:


            return ResponseGeneratorResult(
                text="That's okay.",
                priority=ResponsePriority.STRONG_CONTINUE,
                needs_prompt=True, state=state,
                cur_entity=self.rg.state_manager.current_state.entity_tracker.cur_entity,
                conditional_state=self.rg.ConditionalState(
                    prev_treelet_str=self.name,
                    next_treelet_str="transition")
            )

        else:

            return ResponseGeneratorResult(
                text="Which country?",
                priority=ResponsePriority.STRONG_CONTINUE,
                needs_prompt=True, state=state,
                cur_entity=self.rg.state_manager.current_state.entity_tracker.cur_entity,
                conditional_state=self.rg.ConditionalState(
                    prev_treelet_str=self.name,
                    prompt_treelet=self.rg.ask_aspects_treelet.name
                )
            )








