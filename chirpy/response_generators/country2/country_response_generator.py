import logging
from typing import Optional

from chirpy.core.response_generator import ResponseGenerator
from chirpy.core.response_priority import ResponsePriority, PromptType
from chirpy.core.response_generator_datatypes import emptyResult, ResponseGeneratorResult, PromptResult, emptyPrompt, \
    UpdateEntity, AnswerType
from chirpy.core.regex.regex_template import RegexTemplate
from chirpy.core.regex.response_lists import RESPONSE_TO_THATS, RESPONSE_TO_DIDNT_KNOW

from chirpy.response_generators.country2.treelets.introductory_treelet import IntroductoryTreelet
# from chirpy.response_generators.country2.treelets.ask_ever_been_there_treelet import AskEverBeenThereTreelet
# from chirpy.response_generators.country2.treelets.handle_ever_been_there import HandleEverBeenThereTreelet
# from chirpy.response_generators.country2.treelets.ask_favorite_place_treelet import AskFavoritePlaceTreelet

from chirpy.response_generators.country2.treelets.favorite_country_treelet import FavoriteCountryTreelet
from chirpy.response_generators.country2.treelets.ever_been_country_treelet import EverBeenThereTreelet
from chirpy.response_generators.country2.treelets.favorite_place_treelet import FavoritePlaceTreelet
from chirpy.response_generators.country2.treelets.comment_about_favorite_country_treelet import CommentAboutFavoriteCountryTreelet
from chirpy.response_generators.country2.treelets.doubt_about_favorite_country_treelet import DoubtAboutFavoriteCountryTreelet
from chirpy.response_generators.country2.treelets.food_favorite_country_treelet import FoodFavoriteCountryTreelet
from chirpy.response_generators.country2.treelets.learn_about_country_treelet import LearnAboutCountryTreelet
from chirpy.response_generators.country2.treelets.next_country_suggestion_treelet import NextCountrySuggestionTreelet
from chirpy.response_generators.country2.treelets.handle_unspecified_country_treelet import HandleUnspecifiedCountryTreelet
from chirpy.response_generators.country2.treelets.ask_aspects_treelet import AskAspectsTreelet

from chirpy.response_generators.country2.state import State, ConditionalState

from chirpy.response_generators.country2.country_helpers import *

logger = logging.getLogger('chirpylogger')

class Country2ResponseGenerator(ResponseGenerator):
    name = 'COUNTRY2'

    def __init__(self, state_manager) -> None:
        self.introductory_treelet = IntroductoryTreelet(self)
        # self.ask_ever_been_there_treelet = AskEverBeenThereTreelet(self)
        # self.handle_ever_been_there_treelet = HandleEverBeenThereTreelet(self)
        # self.ask_favorite_place_treelet = AskFavoritePlaceTreelet(self)

        self.favorite_country_treelet = FavoriteCountryTreelet(self)
        self.ever_been_country_treelet = EverBeenThereTreelet(self)
        self.favorite_place_treelet = FavoritePlaceTreelet(self)
        self.comment_about_favorite_country_treelet = CommentAboutFavoriteCountryTreelet(self)
        self.doubt_about_favorite_country_treelet = DoubtAboutFavoriteCountryTreelet(self)
        self.food_favorite_country_treelet = FoodFavoriteCountryTreelet(self)
        self.learn_about_country_treelet = LearnAboutCountryTreelet(self)
        self.next_country_suggestion_treelet = NextCountrySuggestionTreelet(self)
        self.handle_unspecified_country_treelet = HandleUnspecifiedCountryTreelet(self)
        self.ask_aspects_treelet = AskAspectsTreelet(self)

        treelets = {
            treelet.name: treelet for treelet in [self.introductory_treelet,
                                                  self.favorite_country_treelet,
                                                  self.ever_been_country_treelet,
                                                  self.favorite_place_treelet,
                                                  self.comment_about_favorite_country_treelet,
                                                  self.doubt_about_favorite_country_treelet,
                                                  self.food_favorite_country_treelet,
                                                  self.learn_about_country_treelet,
                                                  self.next_country_suggestion_treelet,
                                                  self.handle_unspecified_country_treelet,
                                                  self.ask_aspects_treelet
                                                  ]

                                                  # self.ask_ever_been_there_treelet,
                                                  # self.handle_ever_been_there_treelet,
                                                  # self.ask_favorite_place_treelet]
        }
        super().__init__(state_manager, treelets=treelets, can_give_prompts=True,
                         state_constructor=State,
                         conditional_state_constructor=ConditionalState)

    def identify_response_types(self, utterance):
        response_types = super().identify_response_types(utterance)

        if contains_country_keywords(self, utterance):
            response_types.add(ResponseType.COUNTRY_KEYWORDS)

        if contains_food_keywords(self, utterance):
            response_types.add(ResponseType.FOOD_KEYWORDS)

        if contains_specific_country(self, utterance):
            response_types.add(ResponseType.COUNTRY)

        if contains_economy(self, utterance):
            response_types.add(ResponseType.ECONOMY)

        if contains_geography(self, utterance):
            response_types.add(ResponseType.GEOGRAPHY)

        if contains_language(self, utterance):
            response_types.add(ResponseType.LANGUAGE)

        if contains_cuisine(self, utterance):
            response_types.add(ResponseType.CUISINE)

        return response_types

    def get_intro_treelet_response(self) -> Optional[ResponseGeneratorResult]:
        if ResponseType.COUNTRY_KEYWORDS in self.response_types:
            return self.introductory_treelet.get_response(priority=ResponsePriority.FORCE_START)
