import logging
import random

from chirpy.core.response_generator import Treelet
from chirpy.core.response_priority import ResponsePriority
from chirpy.core.response_generator_datatypes import ResponseGeneratorResult, PromptResult, PromptType, AnswerType
from chirpy.response_generators.dinosaur.dinosaur_helpers import ResponseType
from chirpy.response_generators.dinosaur.state import ConditionalState

from chirpy.response_generators.dinosaur.regex_templates.word_lists import SUGGESTED_DINOSAUR

import inflect
engine = inflect.engine()

logger = logging.getLogger('chirpylogger')

AGREEMENT = ["I like {} too!",
            "{} is my favorite as well!",
            "Interesting choice!"]

class IntroduceDinosaurTreelet(Treelet):
    name = "introduce_dinosaur_treelet"

    def __init__(self, rg):
        super().__init__(rg)
        self.can_prompt = True

    def get_prompt(self, conditional_state=None):
        state, utterance, response_types = self.get_state_utterance_response_types()

        return PromptResult(
            text="Would you like us to introduce you to some dinosaur?",
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
                text=f"No worries ...",
                priority=ResponsePriority.STRONG_CONTINUE,
                needs_prompt=True, state=state,
                cur_entity=self.rg.get_current_entity(),
                conditional_state=self.rg.ConditionalState(
                    prev_treelet_str=self.name,
                    prompt_treelet="transition"
                )
            )

        else:
            cur_dinosaur = SUGGESTED_DINOSAUR
            while cur_dinosaur in state.responses_used:
                cur_dinosaur = random.choice(SUGGESTED_DINOSAUR)

            responses_used = state.responses_used
            responses_used.append(cur_dinosaur)

            introduction = f"Let's talk about {cur_dinosaur.talkable_name}"

            is_plural = self.rg.state.cur_dinosaur.is_plural
            copula = infl('are', is_plural)

            neural_response = self.rg.get_neural_response(
                prefix=f"{self.rg.state.cur_dinosaur.talkable_name} {copula}")
            neural_response = neural_response.split('.')[0] + '.'

            return ResponseGeneratorResult(
                text= introduction+neural_response,
                priority=ResponsePriority.STRONG_CONTINUE,
                needs_prompt=False, state=state,
                cur_entity=self.rg.get_current_entity(),
                conditional_state=self.rg.ConditionalState(
                    prev_treelet_str=self.name,
                    prompt_treelet=self.rg.specific_question_treelet.name,
                    cur_dinosaur = cur_dinosaur,
                    responses_used=responses_used
                )
        )

