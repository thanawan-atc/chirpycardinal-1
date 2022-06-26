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



import inflect
engine = inflect.engine()

logger = logging.getLogger('chirpylogger')


class AskFavoritePlaceTreelet(Treelet):
    name = "ask_favorite_place_treelet"


    def get_response(self, priority=ResponsePriority.STRONG_CONTINUE):
        state, utterance, response_types = self.get_state_utterance_response_types()
        place = extract_place(self.rg)


        if place in PLACE:
            conditional_state = self.rg.ConditionalState(
                    prev_treelet_str=self.name,
                    next_treelet_str="transition",
                )
            if place is not None:
                conditional_state.cur_place = place
            return ResponseGeneratorResult(
                text=f"I would like to go to {place} some day as well.",
                priority=ResponsePriority.STRONG_CONTINUE,
                needs_prompt=False, state=state,
                cur_entity=self.rg.state_manager.current_state.entity_tracker.cur_entity,
                conditional_state=conditional_state
            )
        else:
            conditional_state = self.rg.ConditionalState(
                prev_treelet_str=self.name,
                next_treelet_str="transition"
            )

            if place is not None:
                conditional_state.cur_place = place

            return ResponseGeneratorResult(
                text=f"Personally, I want to go to {COUNTRY[state.cur_country]['famous_place']}.",   # Doesn't work yet
                priority=ResponsePriority.STRONG_CONTINUE,
                needs_prompt=False, state=state,
                cur_entity=self.rg.state_manager.current_state.entity_tracker.cur_entity,
                conditional_state=conditional_state
            )



