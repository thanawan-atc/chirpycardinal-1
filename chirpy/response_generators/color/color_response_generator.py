import logging
from typing import Optional

from chirpy.core.response_generator import ResponseGenerator
from chirpy.core.response_priority import ResponsePriority, PromptType
from chirpy.core.response_generator_datatypes import emptyResult, ResponseGeneratorResult, PromptResult, emptyPrompt, \
    UpdateEntity, AnswerType
from chirpy.core.regex.regex_template import RegexTemplate
from chirpy.core.regex.response_lists import RESPONSE_TO_THATS, RESPONSE_TO_DIDNT_KNOW

from chirpy.response_generators.color.treelets.ask_favorite_color_treelet import AskFavoriteColorTreelet
from chirpy.response_generators.color.state import State, ConditionalState

from chirpy.response_generators.color.color_helpers import *

logger = logging.getLogger('chirpylogger')

class ColorResponseGenerator(ResponseGenerator):
    name = 'COLOR'

    def __init__(self, state_manager) -> None:
        self.ask_favorite_color_treelet = AskFavoriteColorTreelet(self)
        treelets = {
            treelet.name: treelet for treelet in [self.ask_favorite_color_treelet]
        }
        super().__init__(state_manager, treelets=treelets, intent_templates=[], can_give_prompts=True,
                         state_constructor=State,
                         conditional_state_constructor=ConditionalState,
                         trigger_words=["color"])

    def identify_response_types(self, utterance):
        response_types = super().identify_response_types(utterance)

        if is_recognized_color(self, utterance):
            response_types.add(ResponseType.RECOGNIZED_COLOR)

        return response_types


