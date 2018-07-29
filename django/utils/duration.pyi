from datetime import timedelta
from typing import Tuple


def _get_duration_components(duration: timedelta) -> Tuple[int, int, int, int, int]: ...


def duration_iso_string(duration: timedelta) -> str: ...


def duration_microseconds(delta: timedelta) -> int: ...


def duration_string(duration: timedelta) -> str: ...