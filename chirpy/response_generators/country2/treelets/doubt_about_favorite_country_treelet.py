import logging
from chirpy.core.regex.regex_template import RegexTemplate
from chirpy.core.regex.util import OPTIONAL_TEXT, NONEMPTY_TEXT, OPTIONAL_TEXT_PRE, OPTIONAL_TEXT_POST, \
    OPTIONAL_TEXT_MID
from chirpy.core.response_generator_datatypes import PromptType, ResponseGeneratorResult, PromptResult, emptyResult, AnswerType
from chirpy.core.response_priority import ResponsePriority, PromptType
from chirpy.core.entity_linker.entity_groups import ENTITY_GROUPS_FOR_EXPECTED_TYPE
from chirpy.core.response_generator import Treelet
from chirpy.response_generators.country2.country_helpers import *
from chirpy.response_generators.country2.state import State, ConditionalState

from chirpy.core.entity_linker.entity_groups import EntityGroupsForExpectedType

import inflect
engine = inflect.engine()

logger = logging.getLogger('chirpylogger')


class DoubtAboutFavoriteCountryTreelet(Treelet):
    name = "doubt_about_favorite_country_treelet"

    def get_prompt(self, conditional_state=None):
        state, utterance, response_types = self.get_state_utterance_response_types()

        return PromptResult(text=f"Then, why is {self.rg.state.cur_country.talkable_name} your favorite country?",
                            prompt_type=PromptType.CURRENT_TOPIC,
                            cur_entity=self.rg.get_current_entity(),
                            state=state, conditional_state=conditional_state)


    def get_response(self, priority=ResponsePriority.STRONG_CONTINUE):
        state, utterance, response_types = self.get_state_utterance_response_types()

        acknowledgement = f"Got you! You now make me want to visit {self.rg.state.cur_country.talkable_name} once soon."

        return ResponseGeneratorResult(
            text= acknowledgement,
            priority=ResponsePriority.STRONG_CONTINUE,
            needs_prompt=True, state=state,
            cur_entity=self.rg.state_manager.current_state.entity_tracker.cur_entity,
            conditional_state=self.rg.ConditionalState(
                prev_treelet_str=self.name,
                next_treelet_str="transition")
        )




