from dataclasses import dataclass
from typing import List, Dict

from tests.utils.nest_A import NestA


@dataclass
class ClassA:

    mandatory_val: str
    nest_val: NestA
    custom_map_val: str
    primitive_list: List[int]
    nest_list: List[NestA]
    primitive_dict: Dict[str, str]
    nest_dict: Dict[str, NestA]
    color: str
