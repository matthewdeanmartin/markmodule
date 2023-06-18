"""
StringLoader
Credit - https://stackoverflow.com/a/62492464/33264

Usage:
with open("testmodule.py", "r") as module:
    load_from_string(module.read(), "testmodule")
"""
import importlib.abc
import importlib.util
import sys


# pylint: disable=too-many-ancestors
class StringLoader(importlib.abc.SourceLoader):
    """Another string loader"""

    def __init__(self, data):
        self.data = data

    def get_source(self, fullname):
        return self.data

    def get_data(self, path):
        return self.data.encode("utf-8")

    def get_filename(self, fullname):
        return "<not a real path>/" + fullname + ".py"


def load_from_string(code: str, module_name: str) -> None:
    """Helper for StringLoader"""
    loader = StringLoader(code)
    spec = importlib.util.spec_from_loader(module_name, loader, origin="built-in")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
