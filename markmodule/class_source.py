"""
Get Class source for de/serialization
"""
import inspect
from typing import Any


def serialize_source(obj: Any) -> str:
    """Look up source code for object"""
    return inspect.getsource(obj)
