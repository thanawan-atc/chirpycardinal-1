import logging
import random

from chirpy.core.response_generator import Treelet
from chirpy.core.response_priority import ResponsePriority
from chirpy.core.response_generator_datatypes import ResponseGeneratorResult, PromptResult, PromptType, AnswerType
from chirpy.response_generators.country2.country_helpers import ResponseType
from chirpy.response_generators.country2.state import ConditionalState

logger = logging.getLogger('chirpylogger')


class FavoriteCountryTreelet(Treelet):
    name = "favorite_country_treelet"

    def __init__(self, rg):
        super().__init__(rg)
        self.can_prompt = True

    def get_prompt(self, conditional_state=None):
        state, utterance, response_types = self.get_state_utterance_response_types()

        return PromptResult(
            text="By the way, what's your favorite country?",
            state=state,
            cur_entity=self.rg.get_current_entity(),
            conditional_state=conditional_state,
            prompt_type=PromptType.CURRENT_TOPIC,
            answer_type=AnswerType.QUESTION_SELFHANDLING
        )

    def get_response(self, priority=ResponsePriority.STRONG_CONTINUE):
        state, utterance, response_types = self.get_state_utterance_response_types()

        cur_country = self.rg.get_current_entity()

        return ResponseGeneratorResult(
            text=f"I like {cur_country.talkable_name} too!",
            priority=ResponsePriority.STRONG_CONTINUE,
            needs_prompt=False, state=state,
            cur_entity=self.rg.get_current_entity(),
            conditional_state=self.rg.ConditionalState(
                prev_treelet_str=self.name,
                prompt_treelet=self.rg.ever_been_country_treelet.name,
                cur_country = cur_country
            )
        )
