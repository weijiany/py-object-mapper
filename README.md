# py-object-mapper

A mapper is used to map an object to other object.

The package is easy to custom mapping for any fields.

## How to use it?

The origin class:

```python
from dataclasses import dataclass

@dataclass
class ClassA:

    mandatory_val: str
```

The target clas:

```python
from dataclasses import dataclass

@dataclass
class ClassB:

    mandatory_val: str
```

Demo like this.
```python
from py_object_mapper import register_map, map_obj

register_map(ClassA, ClassB)
to_obj = map_obj(ClassA("123"), ClassB)

# to_obj <ClassB> mandatory_val="123"
```

More detail can refer to: [unit test](https://github.com/weijiany/py-object-mapper/blob/master/tests/test_mapper.py).
