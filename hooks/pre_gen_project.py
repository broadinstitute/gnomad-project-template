import re
import sys

if not re.match(r"^[a-z][_a-z0-9]+$", "{{ cookiecutter.package_name }}"):
    print(
        "package name should contain only lower case letters, underscores, and numbers",
        file=sys.stderr,
    )
    sys.exit(1)
