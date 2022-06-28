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

AGREEMENT = ["I totally agree! ", "I couldn't agree more! "]

class CommentAboutFavoriteCountryTreelet(Treelet):
    name = "comment_about_favorite_country_treelet"

    def get_prompt(self, conditional_state=None):
        state, utterance, response_types = self.get_state_utterance_response_types()

        return PromptResult(text="What do you like about it?",
                            prompt_type=PromptType.CURRENT_TOPIC,
                            cur_entity=self.rg.get_current_entity(),
                            state=state, conditional_state=conditional_state)

    def get_response(self, priority=ResponsePriority.STRONG_CONTINUE):
        state, utterance, response_types = self.get_state_utterance_response_types()

        is_plural = self.rg.state.cur_country.is_plural
        copula = infl('are', is_plural)

        acknowledgement = random.choice(AGREEMENT)
        neural_response = self.rg.get_neural_response(
            prefix=f"{self.rg.state.cur_country.talkable_name} {copula} very well known for")
        neural_response = neural_response.split('.')[0] + '.'


        return ResponseGeneratorResult(
            text= acknowledgement + neural_response,
            priority=ResponsePriority.STRONG_CONTINUE,
            needs_prompt=True, state=state,
            cur_entity=self.rg.state_manager.current_state.entity_tracker.cur_entity,
            conditional_state=self.rg.ConditionalState(
                prev_treelet_str=self.name,
                next_treelet_str="transition")
        )