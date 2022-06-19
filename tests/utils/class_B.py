from dataclasses import dataclass
from typing import List, Dict

from tests.utils.nest_B import NestB


@dataclass
class ClassB:

    mandatory_val: str
    nest_val: NestB
    custom_map_val: str
    primitive_list: List[int]
    nest_list: List[NestB]
    primitive_dict: Dict[str, str]
    nest_dict: Dict[str, NestB]
    default_val: int = 10
