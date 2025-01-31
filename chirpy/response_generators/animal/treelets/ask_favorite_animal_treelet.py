import logging
from chirpy.core.regex.regex_template import RegexTemplate
from chirpy.core.regex.util import OPTIONAL_TEXT, NONEMPTY_TEXT, OPTIONAL_TEXT_PRE, OPTIONAL_TEXT_POST, \
    OPTIONAL_TEXT_MID
from chirpy.core.response_generator_datatypes import PromptType, ResponseGeneratorResult, PromptResult, emptyResult, AnswerType
from chirpy.core.response_priority import ResponsePriority, PromptType
from chirpy.core.entity_linker.entity_groups import ENTITY_GROUPS_FOR_EXPECTED_TYPE
from chirpy.core.response_generator import Treelet
from chirpy.response_generators.animal.animal_helpers import *
from chirpy.response_generators.animal.state import State, ConditionalState

import inflect
engine = inflect.engine()

logger = logging.getLogger('chirpylogger')


class AskFavoriteAnimalTreelet(Treelet):
    name = "ask_favorite_animal_treelet"

    def get_response(self, priority=ResponsePriority.STRONG_CONTINUE, **kwargs):
        """ Returns the response.
        :param **kwargs:
        """
        return ResponseGeneratorResult(text="Sure! What's your favorite animal?", priority=ResponsePriority.CAN_START,
                                       needs_prompt=False, state=State(),
                                       cur_entity=None,
                                       answer_type=AnswerType.QUESTION_SELFHANDLING,
                                       conditional_state=ConditionalState(
                                           next_treelet_str="animal_introductory_treelet",
                                           cur_animal=None),
                                       expected_type=ENTITY_GROUPS_FOR_EXPECTED_TYPE.animal_related
                                       )
