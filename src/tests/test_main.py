from __future__ import annotations

from dycw_template import __version__


def test_main() -> None:
    from zoneinfo import ZoneInfo

    zi = ZoneInfo("UTC")

    assert isinstance(zi, ZoneInfo)


def test_main2() -> None:
    import datetime as dt

    zi = dt.UTC

    assert isinstance(zi, ZoneInfo)
