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

class IntroductoryTreelet(Treelet):
    name = "animal_introductory_treelet"

    def get_response(self, priority=ResponsePriority.STRONG_CONTINUE, **kwargs):
        """ Returns the response.
        :param **kwargs:
        """
        state, utterance, response_types = self.get_state_utterance_response_types()
        entity = self.rg.get_current_entity()
        if entity is None: return self.emptyResult()
        cur_animal = entity.name.lower()
        cur_talkable_animal = entity.talkable_name

        logger.primary_info(f"ANIMAL intro treelet examining {cur_animal} ({is_known_animal(cur_animal)})")

        if not is_known_animal(cur_animal):
            logger.error("ANIMAL Intro Treelet was triggered, but current entity is unknown in our database.")
            return self.emptyResult()

        intro = get_intro_acknowledgement(cur_talkable_animal, entity.is_plural)

        pronoun = 'they' if entity.is_plural else 'it'
        copula = 'they\'re' if entity.is_plural else 'it\'s'


        # decide on an internal prompt
        if is_subclassable(cur_animal):
            prompt_treelet = self.rg.comment_on_favorite_type_treelet.name
            text = intro
        else:
            best_attribute, best_attribute_value = get_attribute(cur_animal)
            if best_attribute is not None:
                if best_attribute == 'ingredient':
                    attribute_comment = f"Personally, I especially like the {best_attribute_value} in it, I think it gives {pronoun} a really nice flavor."
                elif best_attribute == 'texture':
                    attribute_comment = f"Personally, I love {pronoun} texture, especially how {copula} so {best_attribute_value}."
                text = f"{intro} {attribute_comment}"
            else:
                neural_response = self.get_neural_response(prefix=f'I especially love how {pronoun}')
                text = f"{intro} {neural_response}"
            prompt_treelet = self.rg.open_ended_user_comment_treelet.name

        # special exceptional activation check
        neural_chat_state = self.rg.state_manager.current_state.response_generator_states.get('NEURAL_CHAT', None)
        if neural_chat_state is not None and getattr(neural_chat_state, 'next_treelet', None):
            priority = ResponsePriority.FORCE_START

        return ResponseGeneratorResult(text=text, priority=priority,
                                       needs_prompt=False, state=state,
                                       cur_entity=entity,
                                       conditional_state=ConditionalState(cur_animal=entity,
                                                                          prompt_treelet=prompt_treelet))

    def get_prompt(self, **kwargs):
        return None
