import logging
from chirpy.core.regex.regex_template import RegexTemplate
from chirpy.core.regex.util import OPTIONAL_TEXT, NONEMPTY_TEXT, OPTIONAL_TEXT_PRE, OPTIONAL_TEXT_POST, \
    OPTIONAL_TEXT_MID
from chirpy.core.response_generator_datatypes import PromptType, ResponseGeneratorResult, PromptResult, emptyResult, \
    AnswerType
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


class LearnAboutCountryTreelet(Treelet):
    name = "learn_about_country_treelet"

    def get_prompt(self, conditional_state=None):
        state, utterance, response_types = self.get_state_utterance_response_types()

        cur_country = self.rg.state.cur_country

        return PromptResult(text=f"Anyway, thank you for sharing about {cur_country.talkable_name}. "
                                 f"Is there any country you want to learn more about?",
                            prompt_type=PromptType.CURRENT_TOPIC,
                            cur_entity=self.rg.get_current_entity(),
                            state=state, conditional_state=conditional_state)

    def get_response(self, priority=ResponsePriority.STRONG_CONTINUE):
        state, utterance, response_types = self.get_state_utterance_response_types()

        if ResponseType.NO in response_types:

            new_country = random.choice(COUNTRY)
            while new_country in state.responses_used:
                new_country = random.choice(COUNTRY)

            responses_used = state.responses_used
            responses_used.append(new_country)

            return ResponseGeneratorResult(
                text=f"We could talk about {new_country} if you'd like.",
                priority=ResponsePriority.STRONG_CONTINUE,
                needs_prompt=False, state=state,
                cur_entity=self.rg.state_manager.current_state.entity_tracker.cur_entity,
                conditional_state=self.rg.ConditionalState(
                    prev_treelet_str=self.name,
                    next_treelet_str=self.rg.handle_next_country_suggestion_treelet.name,
                    cur_country=new_country,
                    responses_used=responses_used
                )
            )

        elif ResponseType.COUNTRY in response_types:
            cur_country = self.rg.get_current_entity()

            return ResponseGeneratorResult(
                text="Sure!",
                priority=ResponsePriority.STRONG_CONTINUE,
                needs_prompt=False, state=state,
                cur_entity=self.rg.state_manager.current_state.entity_tracker.cur_entity,
                conditional_state=self.rg.ConditionalState(
                    prev_treelet_str=self.name,
                    prompt_treelet=self.rg.ask_aspects_treelet.name,
                    cur_country=cur_country
                )
            )

        else:
            return ResponseGeneratorResult(
                text="Which country?",
                priority=ResponsePriority.STRONG_CONTINUE,
                needs_prompt=False, state=state,
                cur_entity=self.rg.state_manager.current_state.entity_tracker.cur_entity,
                conditional_state=self.rg.ConditionalState(
                    prev_treelet_str=self.name,
                    next_treelet_str=self.rg.handle_unspecified_country_treelet.name
                ),
                answer_type=AnswerType.QUESTION_SELFHANDLING
            )







