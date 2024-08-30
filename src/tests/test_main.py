from __future__ import annotations

from utilities.zoneinfo import UTC, get_time_zone_name

from dycw_template import __version__


def test_main() -> None:
    assert get_time_zone_name(UTC) == "UTC"
