import inspect
from typing import Type, List, Tuple


def __param_infos(a_type: Type) -> List[Tuple[str, inspect.Parameter]]:
    return [param for param in inspect.signature(a_type.__init__).parameters.items() if param[0] != "self"]


def mandatory_params(a_type: Type) -> List[Tuple[str, inspect.Parameter]]:
    return [param for param in __param_infos(a_type) if param[1].default == inspect.Parameter.empty]


def optional_params(a_type: Type) -> List[Tuple[str, inspect.Parameter]]:
    return [param for param in __param_infos(a_type) if param[1].default != inspect.Parameter.empty]
