from __future__ import annotations

import datetime as dt
from typing import cast

from utilities.platform import SYSTEM, System
from utilities.zoneinfo import HONG_KONG, UTC, ensure_time_zone, get_time_zone_name
from whenever import ZonedDateTime


def test_main() -> None:
    assert get_time_zone_name(UTC) == "UTC"
    datetime = dt.datetime(1951, 4, 1, 3, tzinfo=HONG_KONG)
    time_zone = ensure_time_zone(cast(dt.timezone, datetime.tzinfo))
    datetime2 = datetime.replace(tzinfo=time_zone)
    match SYSTEM:
        case System.windows:
            use = "Etc/UTC"
        case _:
            use = "UTC"
    _ = ZonedDateTime.from_py_datetime(datetime2).to_tz(use)
