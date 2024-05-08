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

    template_dashed = "template-python"
    template_underscore = template_dashed.replace("-", "_")

    name = get_repo_name()
    name_dashed = name.replace("_", "-")
    name_underscore = name.replace("-", "_")

    for dashed, name in [
        (template_dashed, name_dashed),
        (template_underscore, name_underscore),
    ]:
        process_root(root, dashed, name)


def process_root(root: Path, template: str, name: str, /) -> None:
    _LOGGER.info("Processing %s (%s -> %s)", root, template, name)
    for path in root.iterdir():
        if path.is_file():
            with path.open() as fh:
                old_contents = fh.read()
            new_contents = sub(template, name, old_contents)
            if old_contents != new_contents:
                _LOGGER.info("Re-writing %s...", path)
                with path.open(mode="w") as fh:
                    _ = fh.write(new_contents)
    for path in list(root.iterdir()):
        old_stem = path.stem
        new_stem = sub(template, name, old_stem)
        new_path = path.with_stem(new_stem)
        if path != new_path:
            _LOGGER.info("Renaming %s -> %s...", path, new_path)
            _ = path.rename(new_path)


if __name__ == "__main__":
    main()
