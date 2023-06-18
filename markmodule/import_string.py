"""
Import python code from codeblocks in a markdown file as a module.

Danger! This executes code. Don't do this unless you control the serialization and deserialization.
"""
import importlib.util
import pathlib
import sys

import mistune


def import_md(name: str) -> None:
    """Import markdown file"""
    path = pathlib.Path(name)
    suffix = path.suffix
    if not suffix:
        path = pathlib.Path(name + ".md")
    with open(path, encoding="utf-8") as file:
        string_value = file.read()
        import_markdown_string(string_value, path.stem)


def import_markdown_string(string_value: str, module_name: str) -> None:
    """Import markdown as a string."""
    parser = mistune.create_markdown(renderer="ast")

    if mistune.__version__.startswith("3"):
        result, _block_state = parser.parse(string_value)
    else:
        result = parser.parse(string_value)

    code_string = ""
    for token in result:
        if token["type"] == "blank_line":
            continue
        if mistune.__version__.startswith("3."):
            if token["type"] == "block_code" and token.get("attrs", {}).get("info") in (
                "python",
                "python3",
                "py",
            ):
                code_string += token["raw"]
        else:
            if token["type"] == "block_code" and token["info"] == "python":
                code_string += token["text"]

    if not code_string:
        raise TypeError("Can't find source code in markdown file")
    import_code_string(code_string, module_name)


def import_code_string(code_string: str, module_name: str) -> None:
    """Import a code string as a module using function. See md_module_support to import
    using `import` syntax."""
    spec = importlib.util.spec_from_loader(module_name, loader=None)
    if not spec:
        raise TypeError("Failed to initialize a module spec with that module name")
    module = importlib.util.module_from_spec(spec)

    # pylint: disable=exec-used
    exec(code_string, module.__dict__)
    sys.modules[module_name] = module
