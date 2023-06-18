"""
Usage
sys.meta_path.append(MdFinder())

Created with help from ChatGPT
"""
import importlib.abc
import importlib.util
import os
import sys
from modulefinder import Module
from typing import Optional

from markmodule.import_string import parse_code_out_of_markdown


# pylint: disable=too-many-ancestors
class MdImporter(importlib.abc.SourceLoader):
    """Syntactic sugar for import"""

    def __init__(self, path):
        self.path = path
        self.code = None

    def create_module(self, spec):
        """This method may return None, indicating that default module creation
        semantics should take place."""
        return None

    # pylint: disable=unused-argument
    def get_data(self, path: str) -> None:
        """For returning byte code... I think. Not implemented"""
        return None

    # pylint: disable=unused-argument
    def exec_module(self, module: Module) -> None:
        """Execute code and load up as a module"""
        with open(self.path, encoding="utf-8") as file:
            markdown = file.read()
            self.code = parse_code_out_of_markdown(markdown)
        # pylint: disable=exec-used
        exec(self.code, module.__dict__)

    # pylint: disable=unused-argument
    def get_filename(self, fullname: str) -> str:
        """Path that source came from."""
        return self.path

    # pylint: disable=unused-argument
    def get_source(self, fullname: str) -> str:
        """Source for debuggers"""
        return self.code


class MdFinder(importlib.abc.MetaPathFinder):
    """Allow for import syntax to work."""

    # pylint: disable=unused-argument
    def find_spec(self, fullname: str, path: str, target: Optional[str] = None):
        """Find a markdown file and load it as a module"""
        md_path = fullname.replace(".", "/") + ".md"
        for sys_path in sys.path:
            full_path = sys_path + "/" + md_path
            if os.path.exists(full_path):
                return importlib.util.spec_from_loader(fullname, MdImporter(full_path), origin=full_path)

        return None
