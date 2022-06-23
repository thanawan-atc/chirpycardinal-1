import logging
from chirpy.core.regex.regex_template import RegexTemplate
from chirpy.core.response_generator_datatypes import PromptType, ResponseGeneratorResult, PromptResult, AnswerType
from chirpy.core.response_priority import ResponsePriority, PromptType
from chirpy.core.entity_linker.entity_groups import ENTITY_GROUPS_FOR_EXPECTED_TYPE
from chirpy.core.response_generator import Treelet
from chirpy.response_generators.country.country_helpers import *
from chirpy.core.entity_linker.entity_groups import EntityGroupsForExpectedType
from chirpy.core.util import infl
from chirpy.response_generators.country.state import State, ConditionalState

logger = logging.getLogger('chirpylogger')

class AskWhyFavoriteCountryTreelet(Treelet):
    name = "ask_why_favorite_country_treelet"

    def get_response(self, priority=ResponsePriority.STRONG_CONTINUE, **kwargs):
        """ Returns the response. """
        state, utterance, response_types = self.get_state_utterance_response_types()
        entity = self.rg.get_current_entity(initiated_this_turn=False)
        cur_country_entity = state.cur_country
        cur_country = cur_country_entity.name

        user_answer, is_plural = self.get_best_candidate_user_entity(utterance, cur_country)
        copula = infl('are', is_plural)
        pronoun = infl('they', is_plural)


        entity = self.rg.state_manager.current_state.entity_tracker.cur_entity
        text = f"That totally makes sense! I also really like {user_answer}. Personally, I really like the food there."

        return ResponseGeneratorResult(text=text, priority=priority,
                                       needs_prompt=False, state=state,
                                       cur_entity=entity,
                                       conditional_state=ConditionalState(
                                           next_treelet_str="transition",
                                           cur_country=cur_country_entity)
                                       )
