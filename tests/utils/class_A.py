from dataclasses import dataclass

from tests.utils.nest_A import NestA


@dataclass
class ClassA:

    mandatory_val: str
    nest_val: NestA
