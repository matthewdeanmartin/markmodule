from mypyc.build import mypycify
from setuptools import setup

setup(
    name="markmodule",
    packages=["markmodule"],
    ext_modules=mypycify(
        [
            "--disallow-untyped-defs",  # Pass a mypy flag
            "markmodule",
        ]
        # , opt_level="3", debug_level="1"
    ),
)
