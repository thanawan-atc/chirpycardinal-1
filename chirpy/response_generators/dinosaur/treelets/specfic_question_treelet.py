import logging
import random

from chirpy.core.response_generator import Treelet
from chirpy.core.response_priority import ResponsePriority
from chirpy.core.response_generator_datatypes import ResponseGeneratorResult, PromptResult, PromptType, AnswerType
from chirpy.response_generators.dinosaur.dinosaur_helpers import ResponseType
from chirpy.response_generators.dinosaur.state import ConditionalState

from chirpy.response_generators.wiki2.wiki_response_generator import WikiResponseGenerator

import inflect
engine = inflect.engine()

logger = logging.getLogger('chirpylogger')


class SpecificQuestionTreelet(Treelet):
    name = "specific_question_treelet"

    def __init__(self, rg):
        super().__init__(rg)
        self.can_prompt = True

    def get_prompt(self, conditional_state=None):
        state, utterance, response_types = self.get_state_utterance_response_types()

        return PromptResult(
            text="/To DO",
            state=state,
            cur_entity=self.rg.get_current_entity(),
            conditional_state=conditional_state,
            prompt_type=PromptType.CURRENT_TOPIC,
            answer_type=AnswerType.QUESTION_SELFHANDLING
        )

    def get_response(self, priority=ResponsePriority.STRONG_CONTINUE):
        state, utterance, response_types = self.get_state_utterance_response_types()

        return ResponseGeneratorResult(
            text="TODO",
            priority=ResponsePriority.STRONG_CONTINUE,
            needs_prompt=True, state=state,
            cur_entity=self.rg.get_current_entity(),
            conditional_state=self.rg.ConditionalState(
                prev_treelet_str=self.name,
                next_treelet_str="transition")
        )