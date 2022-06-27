import logging
from chirpy.core.regex.regex_template import RegexTemplate
from chirpy.core.regex.util import OPTIONAL_TEXT, NONEMPTY_TEXT, OPTIONAL_TEXT_PRE, OPTIONAL_TEXT_POST, \
    OPTIONAL_TEXT_MID
import random
from chirpy.core.response_generator_datatypes import PromptType, ResponseGeneratorResult, PromptResult, emptyResult, AnswerType
from chirpy.core.response_priority import ResponsePriority, PromptType
from chirpy.core.entity_linker.entity_groups import ENTITY_GROUPS_FOR_EXPECTED_TYPE
from chirpy.core.response_generator import Treelet
from chirpy.response_generators.country2.country_helpers import *
from chirpy.response_generators.country2.state import State, ConditionalState

from chirpy.response_generators.country2.regex_templates.word_lists import PLACE, COUNTRY

from chirpy.core.entity_linker.entity_groups import EntityGroupsForExpectedType



import inflect
engine = inflect.engine()

logger = logging.getLogger('chirpylogger')


class AskFavoritePlaceTreelet(Treelet):
    name = "ask_favorite_place_treelet"

    def get_best_candidate_user_entity(self, utterance, cur_place):
        def condition_fn(entity_linker_result, linked_span, entity):
            return EntityGroupsForExpectedType.location_related.matches(entity) and entity.name != cur_place
        entity = self.rg.state_manager.current_state.entity_linker.top_ent(condition_fn) or self.rg.state_manager.current_state.entity_linker.top_ent()
        if entity is not None:
            user_answer = entity.talkable_name
            plural = entity.is_plural
        else:
            nouns = self.rg.state_manager.current_state.corenlp['nouns']
            if len(nouns):
                user_answer = nouns[-1]
                plural = True
            else:
                user_answer = utterance.replace('i like', '').replace('my favorite', '').replace('i love', '')
                plural = True

        return user_answer, plural


    def get_response(self, priority=ResponsePriority.STRONG_CONTINUE):
        state, utterance, response_types = self.get_state_utterance_response_types()
        # place = extract_place(self.rg)

        cur_place = self.rg.get_current_entity()


        # logger.primary_info(f"The state class is {ConditionalState}, the state is {state}.")
        # print('+ 1', cur_place)
        # print('+ 2', state.cur_country)
        # print('+ 3', state.cur_place)

        user_answer, is_plural = self.get_best_candidate_user_entity(utterance, state.cur_place)
        copula = infl('are', is_plural)
        pronoun = infl('they', is_plural)

        neural_response = self.rg.get_neural_response(
            prefix=f"{user_answer} {copula} a great choice! I especially love how {pronoun}")

        return ResponseGeneratorResult(
                text=neural_response,
                priority=ResponsePriority.STRONG_CONTINUE,
                needs_prompt=False, state=state,
                cur_entity=self.rg.state_manager.current_state.entity_tracker.cur_entity,
                conditional_state=self.rg.ConditionalState(
                                prev_treelet_str=self.name,
                                next_treelet_str="transition",
                                cur_place=cur_place)
        )

        # if cur_place in PLACE:
        #     conditional_state = self.rg.ConditionalState(
        #             prev_treelet_str=self.name,
        #             next_treelet_str="transition",
        #             cur_place = cur_place
        #         )
        #     # if cur_place is not None:
        #     #     conditional_state.cur_place = place
        #
        #     return ResponseGeneratorResult(
        #         text=f"I would like to go to {cur_place} some day as well.",
        #         priority=ResponsePriority.STRONG_CONTINUE,
        #         needs_prompt=False, state=state,
        #         cur_entity=self.rg.get_current_entity(),
        #         conditional_state=conditional_state
        #     )
        # else:
        #     conditional_state = self.rg.ConditionalState(
        #         prev_treelet_str=self.name,
        #         next_treelet_str="transition",
        #         cur_place=cur_place
        #     )
        #
        #     # if place is not None:
        #     #     conditional_state.cur_place = place
        #
        #     return ResponseGeneratorResult(
        #         text=f"Personally, I want to go to {COUNTRY[state.cur_country]['famous_place']}.",   # Doesn't work yet
        #         priority=ResponsePriority.STRONG_CONTINUE,
        #         needs_prompt=False, state=state,
        #         cur_entity=self.rg.get_current_entity(),
        #         conditional_state=conditional_state
        #     )



