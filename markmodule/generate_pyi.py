"""
Generate .pyi file for .md if it doesn't exist by shelling out to mypy
"""
import hashlib
import os
import subprocess
import sys
import tempfile
from typing import Optional

from markmodule.import_string import parse_code_out_of_markdown


def find_file_on_pythonpath(filename: str, extension: str):
    """Find a file in the same places as the .py files"""
    for path in sys.path:
        filepath = os.path.join(path, filename + extension)
        if os.path.isfile(filepath):
            return filepath
    return None


def calculate_hash(data: str) -> str:
    """Hash it"""
    hash_object = hashlib.md5(data.encode())
    hash_value = hash_object.hexdigest()
    return hash_value


def generate_side_by_side_pyi(module_name: str) -> None:
    """Read markdown and write generated .pyi file for intellisense support"""
    module_path = f"{module_name}.md"
    if not os.path.exists(module_path):
        module_path = find_file_on_pythonpath(module_name, ".md")
    if not module_path or not os.path.exists(module_path):
        raise TypeError(f"Can't find {module_name}")

    with open(module_path, encoding="utf-8") as reader:
        code = parse_code_out_of_markdown(reader.read())
        hash_string = calculate_hash(code)
        hash_comment = f"# {hash_string}\n"
        pyi_name = f"{module_name}.pyi"
        if os.path.exists(pyi_name):
            with open(pyi_name, encoding="utf-8") as prospective_pyi:
                first_line = prospective_pyi.readline()
                if first_line == hash_comment:
                    return

        with open(f"{module_name}.pyi", "w", encoding="utf-8") as writer:
            writer.writelines([hash_comment, "\n"])
            writer.write(generate_pyi_from_code(code))


def generate_pyi_from_code(code_string: str) -> Optional[str]:
    """Generates pyi contents give source code"""
    # Create a temporary directory to hold the code file and generated .pyi stub
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a temporary file for the Python code
        code_file = os.path.join(temp_dir, "code.py")
        with open(code_file, "w", encoding="utf-8") as file:
            file.write(code_string)

        # Generate .pyi stub using mypy and capture stdout
        process = subprocess.run(["stubgen", code_file], capture_output=True, text=True, check=False)

        # Check if mypy encountered an error
        if process.returncode != 0:
            raise TypeError(f"mypy stubgen error message: {process.stderr}")

        # Get the name of the generated .pyi file
        pyi_file = "out/code.pyi"

        # Read the contents of the .pyi file into a string
        with open(pyi_file, encoding="utf-8") as file:
            pyi_contents = file.read()

        # # Delete the temporary files
        os.remove(pyi_file)
        os.rmdir("out")

    return pyi_contents
