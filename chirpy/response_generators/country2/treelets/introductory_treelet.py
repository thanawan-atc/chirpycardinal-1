import logging
import random

from chirpy.core.response_generator import Treelet
from chirpy.core.response_priority import ResponsePriority
from chirpy.core.response_generator_datatypes import ResponseGeneratorResult, PromptResult, PromptType, AnswerType
from chirpy.response_generators.country2.country_helpers import ResponseType
from chirpy.response_generators.country2.state import ConditionalState

logger = logging.getLogger('chirpylogger')


class IntroductoryTreelet(Treelet):
    def __init__(self, rg):
        super().__init__(rg)
        self.name = 'country2_introductory'
        self.can_prompt = True

    def get_response(self, priority=ResponsePriority.STRONG_CONTINUE):
        state, utterance, response_types = self.get_state_utterance_response_types()

        return ResponseGeneratorResult(
            text="As of now, there are 195 universally recognized countries (193 members of the UN plus two non-member observer states the Vatican and Palestine). "
                 "What's your favorite country?",
            priority=ResponsePriority.STRONG_CONTINUE,
            needs_prompt=False, state=state,
            cur_entity=self.rg.get_current_entity(),
            conditional_state=self.rg.ConditionalState(
                prev_treelet_str=self.name,
                next_treelet_str=self.rg.favorite_country_treelet.name
            ),
            answer_type=AnswerType.QUESTION_SELFHANDLING
        )
