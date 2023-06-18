import os
import sys
import markmodule


def test_generate_side_by_side_pyi():
    if os.path.exists("test"):
        markmodule.generate_side_by_side_pyi("test/hello_module")
    else:
        markmodule.generate_side_by_side_pyi("hello_module")


def test_md_finder():
    sys.meta_path.append(markmodule.MdFinder())

    import test.hello_module

    print(test.hello_module.hello_world("yo!"))
