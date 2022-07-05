import logging
from typing import Optional

from chirpy.core.response_generator import ResponseGenerator
from chirpy.core.response_priority import ResponsePriority, PromptType
from chirpy.core.response_generator_datatypes import emptyResult, ResponseGeneratorResult, PromptResult, emptyPrompt, \
    UpdateEntity, AnswerType
from chirpy.core.regex.regex_template import RegexTemplate
from chirpy.core.regex.response_lists import RESPONSE_TO_THATS, RESPONSE_TO_DIDNT_KNOW

from chirpy.response_generators.dinosaur.treelets.introductory_treelet import IntroductoryTreelet
from chirpy.response_generators.dinosaur.treelets.favorite_dinosaur_treelet import FavoriteDinosaurTreelet
from chirpy.response_generators.dinosaur.treelets.why_this_dinosaur_treelet import WhyThiseDinosaurTreelet
from chirpy.response_generators.dinosaur.treelets.ask_next_dinosaur_treelet import AskNextDinosaurTreelet
from chirpy.response_generators.dinosaur.treelets.introduce_dinosaur_treelet import IntroduceDinosaurTreelet
from chirpy.response_generators.dinosaur.treelets.specfic_question_treelet import SpecificQuestionTreelet


from chirpy.response_generators.dinosaur.state import State, ConditionalState
from chirpy.response_generators.dinosaur.dinosaur_helpers import *

logger = logging.getLogger('chirpylogger')

class DinosaurResponseGenerator(ResponseGenerator):
    name = 'DINOSAUR'

    def __init__(self, state_manager) -> None:
        self.introductory_treelet = IntroductoryTreelet(self)
        self.favorite_dinosaur_treelet = FavoriteDinosaurTreelet
        self.why_this_dinosaur_treelet = WhyThiseDinosaurTreelet
        self.ask_next_dinosaur_treelet = AskNextDinosaurTreelet
        self.introduce_dinosaur_treelet = IntroduceDinosaurTreelet
        self.specfic_question_treelet = SpecificQuestionTreelet

        treelets = {
            treelet.name: treelet for treelet in [self.introductory_treelet,
                                                  self.favorite_dinosaur_treelet,
                                                  self.why_this_dinosaur_treelet,
                                                  self.ask_next_dinosaur_treelet,
                                                  self.introduce_dinosaur_treelet,
                                                  self.specfic_question_treelet
                                                  ]

        }
        super().__init__(state_manager, treelets=treelets, can_give_prompts=True,
                         state_constructor=State,
                         conditional_state_constructor=ConditionalState)

    def identify_response_types(self, utterance):
        response_types = super().identify_response_types(utterance)

        if contains_dinosaur_keywords(self, utterance):
            response_types.add(ResponseType.DINOSAUR_KEYWORDS)

        return response_types

    def get_intro_treelet_response(self) -> Optional[ResponseGeneratorResult]:
        if ResponseType.DINOSAUR_KEYWORDS in self.response_types:
            return self.introductory_treelet.get_response(priority=ResponsePriority.FORCE_START)
