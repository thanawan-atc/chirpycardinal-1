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

AGREEMENT = ["I like {} too!",
            "{} is my favorite as well!",
            "Interesting choice!"]

class AskNextDinosaurTreelet(Treelet):
    name = "ask_next_dinosaur_treelet"

    def __init__(self, rg):
        super().__init__(rg)
        self.can_prompt = True

    def get_prompt(self, conditional_state=None):
        state, utterance, response_types = self.get_state_utterance_response_types()

        return PromptResult(
            text="Is there any other kind of dinosaur would you like to talk about?",
            state=state,
            cur_entity=self.rg.get_current_entity(),
            conditional_state=conditional_state,
            prompt_type=PromptType.CURRENT_TOPIC,
            answer_type=AnswerType.QUESTION_SELFHANDLING
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
                    prompt_treelet=self.introduce_dinosaur_treelet.name
                )
            )

        else:
            cur_dinosaur = self.rg.get_current_entity()

            responses_used = state.responses_used
            responses_used.append(cur_dinosaur)

            return ResponseGeneratorResult(
                text="Sure!",
                priority=ResponsePriority.STRONG_CONTINUE,
                needs_prompt=False, state=state,
                cur_entity=self.rg.get_current_entity(),
                conditional_state=self.rg.ConditionalState(
                    prev_treelet_str=self.name,
                    prompt_treelet=self.rg.why_this_dinosaur_treelet.name,
                    cur_dinosaur=cur_dinosaur,
                    responses_used=responses_used
            )
        )

