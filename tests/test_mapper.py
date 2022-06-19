from py_object_mapper.mapper import register_map, map_obj
from tests.utils.class_A import ClassA
from tests.utils.class_B import ClassB
from tests.utils.nest_A import NestA
from tests.utils.nest_B import NestB


class TestMapper:

    def setup_method(self):
        self.from_obj = ClassA("test", NestA("tag"), "custom_map_val")

    def test_should_map_obj_with_unmap_key_in_to_obj(self):
        register_map(ClassA, ClassB)
        to_obj = map_obj(self.from_obj, ClassB)

        assert to_obj.mandatory_val == "test"
        assert to_obj.default_val == 10

    def test_should_map_obj_with_nest_obj(self):
        register_map(ClassA, ClassB)
        register_map(NestA, NestB)
        to_obj = map_obj(self.from_obj, ClassB)

        assert to_obj.nest_val.tag == self.from_obj.nest_val.tag

    def test_should_map_obj_with_lambda_for_map_key(self):
        register_map(ClassA, ClassB, {
            "custom_map_val": lambda obj: obj.custom_map_val.upper()
        })
        to_obj = map_obj(self.from_obj, ClassB)

        assert to_obj.custom_map_val == self.from_obj.custom_map_val.upper()
