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
from chirpy.response_generators.country2.regex_templates.word_lists import PLACE

import inflect
engine = inflect.engine()

logger = logging.getLogger('chirpylogger')


class HandleEverBeenThereTreelet(Treelet):
    name = "handle_ever_been_there_treelet"

    def get_response(self, priority=ResponsePriority.STRONG_CONTINUE):
        state, utterance, response_types = self.get_state_utterance_response_types()

        if ResponseType.YES in response_types:

            return ResponseGeneratorResult(
                text="What is your favorite place there?",
                priority=ResponsePriority.STRONG_CONTINUE,
                needs_prompt=False, state=state,
                cur_entity=self.rg.get_current_entity(),
                conditional_state=self.rg.ConditionalState(
                    prev_treelet_str=self.name,
                    next_treelet_str=self.rg.ask_favorite_place_treelet.name,
                ),
                answer_type=AnswerType.QUESTION_SELFHANDLING
            )

        else:

            neural_response = self.rg.get_neural_response(
                prefix=f"I have never been there as well, but I heard that")

            # text = f"If you have a chance, you should go to {COUNTRY[cur_country]['famous_place']} in {cur_country}!"
            # return ResponseGeneratorResult(
            #     text=text,
            #     priority=ResponsePriority.STRONG_CONTINUE,
            #     needs_prompt=False, state=state,
            #     cur_entity=self.rg.state_manager.current_state.entity_tracker.cur_entity,
            #     conditional_state=self.rg.ConditionalState(
            #         prev_treelet_str=self.name,
            #         next_treelet_str='transition'
            #     )
            # )

            return ResponseGeneratorResult(text=neural_response, priority=ResponsePriority.STRONG_CONTINUE,
                                        needs_prompt=True, state=state,
                                        cur_entity=self.rg.get_current_entity(),
                                        conditional_state=ConditionalState(
                                        prev_treelet_str=self.name,
                                        next_treelet_str='transition')
                                        )
