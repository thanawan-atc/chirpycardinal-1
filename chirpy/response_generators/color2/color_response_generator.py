import logging
from typing import Optional

from chirpy.core.response_generator import ResponseGenerator
from chirpy.core.response_priority import ResponsePriority, PromptType
from chirpy.core.response_generator_datatypes import emptyResult, ResponseGeneratorResult, PromptResult, emptyPrompt, \
    UpdateEntity, AnswerType
from chirpy.core.regex.regex_template import RegexTemplate
from chirpy.core.regex.response_lists import RESPONSE_TO_THATS, RESPONSE_TO_DIDNT_KNOW

from chirpy.response_generators.color2.treelets.introductory_treelet import IntroductoryTreelet
from chirpy.response_generators.color2.treelets.ask_why_favorite_color_treelet import AskWhyFavoriteColorTreelet
from chirpy.response_generators.color2.treelets.comment_color_treelet import CommentColorTreelet
from chirpy.response_generators.color2.state import State, ConditionalState

from chirpy.response_generators.color2.color_helpers import *

logger = logging.getLogger('chirpylogger')

class Color2ResponseGenerator(ResponseGenerator):
    name = 'COLOR2'

    def __init__(self, state_manager) -> None:
        self.introductory_treelet = IntroductoryTreelet(self)
        self.ask_why_favorite_color_treelet = AskWhyFavoriteColorTreelet(self)
        self.comment_color_treelet = CommentColorTreelet(self)
        treelets = {
            treelet.name: treelet for treelet in [self.introductory_treelet,
                                                  self.ask_why_favorite_color_treelet,
                                                  self.comment_color_treelet]
        }
        super().__init__(state_manager, treelets=treelets, can_give_prompts=True,
                         state_constructor=State,
                         conditional_state_constructor=ConditionalState)

    def identify_response_types(self, utterance):
        response_types = super().identify_response_types(utterance)

        if contains_color_keywords(self, utterance):
            response_types.add(ResponseType.COLOR_KEYWORDS)

        if favorite_color_detected(self, utterance):
            response_types.add(ResponseType.FAVORITE_COLOR)

        return response_types

    def get_intro_treelet_response(self) -> Optional[ResponseGeneratorResult]:
        if ResponseType.COLOR_KEYWORDS in self.response_types:
            return self.introductory_treelet.get_response(priority=ResponsePriority.FORCE_START)
