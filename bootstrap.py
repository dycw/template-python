#!/usr/bin/env python3
from __future__ import annotations

from logging import getLogger
from re import sub
from typing import TYPE_CHECKING

from utilities.git import get_repo_name, get_repo_root
from utilities.logging import basic_config

if TYPE_CHECKING:
    from pathlib import Path

basic_config()
_LOGGER = getLogger()


def main() -> None:
    root = get_repo_root()
    _LOGGER.info(root)

    template_dashed = "python-template"
    template_underscore = template_dashed.replace("-", "_")

    name = get_repo_name()
    name_dashed = name.replace("_", "-")
    name_underscore = name.replace("-", "_")
    _LOGGER.info(name, name_dashed)

    for dashed, name in [
        (template_dashed, name_dashed),
        (template_underscore, name_underscore),
    ]:
        process_root(root, dashed, name)


def process_root(root: Path, template: str, name: str, /) -> None:
    for path in root.iterdir():
        if path.is_file():
            with path.open() as fh:
                old_contents = fh.read()
            new_contents = sub(template, name, old_contents)
            with path.open(mode="w") as fh:
                fh.write(new_contents)

            _LOGGER.info(path)


if __name__ == "__main__":
    main()
