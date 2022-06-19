from dataclasses import dataclass

from tests.utils.nest_B import NestB


@dataclass
class ClassB:

    mandatory_val: str
    nest_val: NestB
    default_val: int = 10
