import logging
import random

from chirpy.core.response_generator import Treelet
from chirpy.core.response_priority import ResponsePriority
from chirpy.core.response_generator_datatypes import ResponseGeneratorResult, PromptResult, PromptType, AnswerType
from chirpy.response_generators.country2.country_helpers import ResponseType
from chirpy.response_generators.country2.state import ConditionalState

from chirpy.response_generators.wiki2.wiki_response_generator import WikiResponseGenerator

logger = logging.getLogger('chirpylogger')

AGREEMENT = ["I like {} too!",
            "{} is my favorite as well!",
            "Interesting choice!"]

class FavoriteCountryTreelet(Treelet):
    name = "favorite_country_treelet"

    def __init__(self, rg):
        super().__init__(rg)
        self.can_prompt = True

    def get_prompt(self, conditional_state=None):
        state, utterance, response_types = self.get_state_utterance_response_types()

        return PromptResult(
            text="By the way, what's your favorite country?",
            state=state,
            cur_entity=self.rg.get_current_entity(),
            conditional_state=conditional_state,
            prompt_type=PromptType.CURRENT_TOPIC,
            answer_type=AnswerType.QUESTION_SELFHANDLING
        )

    def get_response(self, priority=ResponsePriority.STRONG_CONTINUE):
        state, utterance, response_types = self.get_state_utterance_response_types()

        cur_country = self.rg.get_current_entity()
        logger.primary_info(f"Cur country wikidata categories is {cur_country.wikidata_categories}")

        acknowledgement = random.choice(AGREEMENT).format(cur_country.talkable_name)
        infilling = ""

        wiki_rg = WikiResponseGenerator(self.rg.state_manager)
        top_res, top_ack = wiki_rg.get_infilling_statement(cur_country)
        logger.primary_info(f"Top res is: {top_res}")
        logger.primary_info(f"Top ack is: {top_ack}")
        if top_res is not None:
            infilling = f"{top_res}.",

        print('+', infilling)

        # War wiki_infiller.py: 146 Couldn't find any specific templates for entity <WikiEntity: France> (confidence=0.976, sum_anchortext_counts=161719)>.                                                                                           [13:27:01.908]
        # Inf favorite_country_tree…:47 Topres is: None[13:27:01.910]
        # Inf favorite_country_tree…:48 Topack is: None

        return ResponseGeneratorResult(
            text= acknowledgement+infilling,
            priority=ResponsePriority.STRONG_CONTINUE,
            needs_prompt=False, state=state,
            cur_entity=self.rg.get_current_entity(),
            conditional_state=self.rg.ConditionalState(
                prev_treelet_str=self.name,
                prompt_treelet=self.rg.ever_been_country_treelet.name,
                cur_country = cur_country
            )
        )
