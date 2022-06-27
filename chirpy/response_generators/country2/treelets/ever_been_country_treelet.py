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

import inflect
engine = inflect.engine()

logger = logging.getLogger('chirpylogger')


class EverBeenThereTreelet(Treelet):
    name = "ever_been_country_treelet"

    def get_prompt(self, conditional_state=None):
        state, utterance, response_types = self.get_state_utterance_response_types()

        # logger.primary_info(f"The state class is {ConditionalState}, the state is {state}.")
        # logger.primary_info(f"Neural response is {self.get_neural_response()}")

        return PromptResult(text="Have you ever been there?",
                            prompt_type=PromptType.CURRENT_TOPIC,
                            cur_entity=self.rg.get_current_entity(),
                            state=state, conditional_state=conditional_state)


    def get_response(self, priority=ResponsePriority.STRONG_CONTINUE):
        state, utterance, response_types = self.get_state_utterance_response_types()

        if ResponseType.YES in response_types:

            return ResponseGeneratorResult(
                text="Wow!",
                priority=ResponsePriority.STRONG_CONTINUE,
                needs_prompt=False, state=state,
                cur_entity=self.rg.get_current_entity(),
                conditional_state=self.rg.ConditionalState(
                    prev_treelet_str=self.name,
                    prompt_treelet=self.rg.comment_about_favorite_country_treelet.name,
                )
            )

        else:
            neural_response = self.rg.get_neural_response(
                prefix=f"I have never been there as well, but I heard that")

            return ResponseGeneratorResult(text=neural_response, priority=ResponsePriority.STRONG_CONTINUE,
                                        needs_prompt=False, state=state,
                                        cur_entity=self.rg.get_current_entity(),
                                        conditional_state=ConditionalState(
                                        prev_treelet_str=self.name,
                                        prompt_treelet=self.rg.favorite_place_treelet.name
                                        ),
                                        answer_type=AnswerType.QUESTION_SELFHANDLING
                                        )