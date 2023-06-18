import platform

import mistune

print(
    "{} {}; markmodule {}".format(
        platform.python_implementation(),
        platform.python_version(),
        mistune.__version__,
    )
)
