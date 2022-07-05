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

from chirpy.core.entity_linker.entity_groups import EntityGroupsForExpectedType

import inflect
engine = inflect.engine()

logger = logging.getLogger('chirpylogger')

COMPLIMENT = ["fabulous", "remarkable!", "fantastic", "incredible"]

class FoodFavoriteCountryTreelet(Treelet):
    name = "food_favorite_country_treelet"

    def get_prompt(self, conditional_state=None):
        state, utterance, response_types = self.get_state_utterance_response_types()

        cur_country = self.rg.state.cur_country.talkable_name
        intro_food = f"{cur_country} cuisine is also {random.choice(COMPLIMENT)}. "

        question = "Have you ever tried any of their food? Is there anything you like?"

        print('+ cur_country', cur_country)
        print('+ intro', intro_food)
        print('+ question', question)
        return PromptResult(text=intro_food+question,
                            prompt_type=PromptType.CURRENT_TOPIC,
                            cur_entity=self.rg.get_current_entity(),
                            state=state, conditional_state=conditional_state)


    def get_response(self, priority=ResponsePriority.STRONG_CONTINUE):
        state, utterance, response_types = self.get_state_utterance_response_types()

        food_wiki = "TODO1"
        food_wiki_description = "TODO2"
        food_text = f"Personally, I like {food_wiki} which is {food_wiki_description}."

        return ResponseGeneratorResult(
            text= food_text,
            priority=ResponsePriority.STRONG_CONTINUE,
            needs_prompt=False, state=state,
            cur_entity=self.rg.get_current_entity(),
            conditional_state=self.rg.ConditionalState(
                prev_treelet_str=self.name,
                prompt_treelet=self.rg.learn_about_country_treelet.name)
        )




