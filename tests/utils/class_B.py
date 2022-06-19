from dataclasses import dataclass
from typing import List

from tests.utils.nest_B import NestB


@dataclass
class ClassB:

    mandatory_val: str
    nest_val: NestB
    custom_map_val: str
    primitive_list: List[int]
    nest_list: List[NestB]
    default_val: int = 10
