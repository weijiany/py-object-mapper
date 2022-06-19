import inspect
from dataclasses import dataclass, field
from typing import TypeVar, Type, Callable, Dict, Any, List, Tuple, Optional

from py_object_mapper import inspection

_FT = TypeVar('_FT')
_TT = TypeVar('_TT')


@dataclass
class Mapper:

    NONE_TYPE: Type[_TT] = type(None)
    primitive_types = [int, str, bool]
    mappings: Dict[Type[_FT], Tuple[Type[_TT], Dict[str, Callable]]] = field(default_factory=dict)

    def add_map(self, from_type: Type[_FT], to_type: Type[_TT], custom_mapping: Dict[str, Callable]):
        if custom_mapping is None:
            custom_mapping = {}
        self.mappings[from_type] = (to_type, custom_mapping)

    def map(self, from_obj: _FT, to_type: Type[_TT]) -> _TT:
        if to_type is self.NONE_TYPE:
            if type(from_obj) not in self.mappings:
                return None
            to_type = self.mappings[type(from_obj)][0]

        return to_type(**(
                self.__copy_params_form(from_obj, inspection.mandatory_params(to_type)) |
                self.__copy_params_form(from_obj, inspection.optional_params(to_type))
        ))

    def __copy_params_form(
            self,
            from_obj: _FT,
            param_infos: List[Tuple[str, inspect.Parameter]]) -> Dict[str, Any]:
        result = {}
        custom_mapping = self.mappings[type(from_obj)][1]
        from_prop = vars(from_obj)
        for param_info in param_infos:
            prop, parameter = param_info
            value_of_from = from_prop.get(prop)

            if prop in custom_mapping:
                value_of_from = custom_mapping[prop](from_obj)
            elif value_of_from is None:
                value_of_from = parameter.default
            elif type(value_of_from) not in self.primitive_types:
                if isinstance(value_of_from, list):
                    value_of_from = self.__mapper_list(value_of_from)
                elif isinstance(value_of_from, dict):
                    value_of_from = self.__mapper_dict(value_of_from) or value_of_from
                else:
                    value_of_from = self.map(value_of_from, self.NONE_TYPE)
            result[prop] = value_of_from
        return result

    def __mapper_dict(self, value_of_from) -> Dict[str, Optional[_TT]]:
        result: Dict[str, Optional[_TT]] = {}
        for key, val in value_of_from.items():
            if type(val) in self.mappings:
                to_model = self.map(val, self.NONE_TYPE)
                result[key] = to_model
        return result

    def __mapper_list(self, value_of_from) -> List[Optional[_TT]]:
        temp_list: List[Optional[_TT]] = []
        for item in value_of_from:
            if type(item) in self.primitive_types:
                temp_list.append(item)
            else:
                temp_list.append(self.map(item, self.NONE_TYPE))
        return temp_list


mapper = Mapper()


def map_obj(from_obj: _FT, to_type: Type[_TT]) -> _TT:
    return mapper.map(from_obj, to_type)


def register_map(from_type: Type[_FT], to_type: Type[_TT], custom_mapping: Dict[str, Callable[[_FT], Any]] = None):
    return mapper.add_map(from_type, to_type, custom_mapping)


__all__ = ["map_obj", "register_map"]

