from typing import Optional

from chirpy.core.response_generator.state import *
from typing import List, Optional
from dataclasses import dataclass, field

@dataclass
class State(BaseState):
    responses_used: List[str] = field(default_factory=list)
    cur_dinosaur: Optional['WikiEntity'] = None
    fav_dinosaur: Optional['WikiEntity'] = None

@dataclass
class ConditionalState(BaseConditionalState):
    responses_used: List[str] = NO_UPDATE
    cur_dinosaur: Optional['WikiEntity'] = NO_UPDATE
    fav_dinosaur: Optional['WikiEntity'] = NO_UPDATE
    prompt_treelet: Optional[str] = NO_UPDATE