from typing import Optional

from chirpy.core.response_generator.state import *

@dataclass
class State(BaseState):
    cur_country = None
    cur_place = None

@dataclass
class ConditionalState(BaseConditionalState):
    cur_country = NO_UPDATE
    cur_place = NO_UPDATE