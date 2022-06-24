import logging
from chirpy.core.regex.regex_template import RegexTemplate
from chirpy.core.regex.util import OPTIONAL_TEXT, NONEMPTY_TEXT, OPTIONAL_TEXT_PRE, OPTIONAL_TEXT_POST, \
    OPTIONAL_TEXT_MID
from chirpy.core.response_generator_datatypes import PromptType, ResponseGeneratorResult, PromptResult, emptyResult, AnswerType
from chirpy.core.response_priority import ResponsePriority, PromptType
from chirpy.core.entity_linker.entity_groups import ENTITY_GROUPS_FOR_EXPECTED_TYPE
from chirpy.core.response_generator import Treelet
from chirpy.response_generators.color2.color_helpers import *
from chirpy.response_generators.color2.state import State, ConditionalState

import inflect
engine = inflect.engine()

logger = logging.getLogger('chirpylogger')


class CommentColorTreelet(Treelet):
    name = "comment_color_treelet"

    def __init__(self, rg):
        super().__init__(rg)
        self.cur_color = None


    def get_response(self, priority):
        state, utterance, response_types = self.get_state_utterance_response_types()


        response = 'I totally agree. Thank you for sharing!'
        needs_prompt = True

        return ResponseGeneratorResult(
            text=response,
            priority=ResponsePriority.STRONG_CONTINUE,
            needs_prompt=needs_prompt, state=state,
            cur_entity=self.rg.state_manager.current_state.entity_tracker.cur_entity,
            conditional_state=self.rg.ConditionalState(
                prev_treelet_str=self.name,
                cur_color=self.cur_color,
                next_treelet_str='transition',
            )
        )
