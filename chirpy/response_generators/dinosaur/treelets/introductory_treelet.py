import logging
import random

from chirpy.core.response_generator import Treelet
from chirpy.core.response_priority import ResponsePriority
from chirpy.core.response_generator_datatypes import ResponseGeneratorResult, PromptResult, PromptType, AnswerType
from chirpy.response_generators.dinosaur.dinosaur_helpers import ResponseType
from chirpy.response_generators.dinosaur.state import ConditionalState

logger = logging.getLogger('chirpylogger')


class IntroductoryTreelet(Treelet):
    def __init__(self, rg):
        super().__init__(rg)
        self.name = 'dinosaur_introductory'
        self.can_prompt = True

    def get_response(self, priority=ResponsePriority.STRONG_CONTINUE):
        state, utterance, response_types = self.get_state_utterance_response_types()

        return ResponseGeneratorResult(
            text="Dinosaurs were a successful group of animals that emerged between 240 million and 230 million years ago "
                 "and came to rule the world until about 66 million years ago, when a giant asteroid slammed into Earth. "
                 "During that time, dinosaurs evolved from a group of mostly dog- and horse-size creatures into the most "
                 "enormous beasts that ever existed on land. What's your favorite dinosaur?",
            priority=ResponsePriority.STRONG_CONTINUE,
            needs_prompt=False, state=state,
            cur_entity=self.rg.get_current_entity(),
            conditional_state=self.rg.ConditionalState(
                prev_treelet_str=self.name,
                next_treelet_str=self.rg.favorite_dinosaur_treelet.name
            ),
            answer_type=AnswerType.QUESTION_SELFHANDLING
        )

