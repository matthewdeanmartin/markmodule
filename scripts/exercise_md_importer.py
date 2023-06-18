import sys
import markmodule

markmodule.generate_side_by_side_pyi("hello_module")

sys.meta_path.append(markmodule.MdFinder())

import hello_module  # noqa: E402

print(hello_module.hello_world("yo!"))
