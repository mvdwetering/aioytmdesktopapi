from .helpers import generate_attribute_string
from .constants import LikeStatus, RepeatType


class Player:
    """Represent Player state."""

    def __init__(self, raw, request) -> None:
        self._raw = raw
        self._request = request

    def __str__(self) -> str:
        attributes = [
            "has_song",
            "is_paused",
            "volume_percent",
            "seekbar_current_position",
            "seekbar_current_position_human",
            "state_percent",
            "like_status",
            "repeat_type",
        ]
        return generate_attribute_string(self, attributes)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Player):
            return NotImplemented
        return self._raw == other._raw

    @property
    def has_song(self) -> bool:
        return self._raw["hasSong"]

    @property
    def is_paused(self) -> bool:
        return self._raw["isPaused"]

    @property
    def volume_percent(self) -> int:
        return self._raw["volumePercent"]

    @property
    def seekbar_current_position(self) -> int:
        return self._raw["seekbarCurrentPosition"]

    @property
    def seekbar_current_position_human(self) -> str:
        return self._raw["seekbarCurrentPositionHuman"]

    @property
    def state_percent(self) -> int:
        return self._raw["statePercent"]

    @property
    def like_status(self) -> LikeStatus:
        return self._raw["likeStatus"]

    @property
    def repeat_type(self) -> RepeatType:
        return self._raw["repeatType"]

    async def update(self) -> None:
        response = await self._request("get", "/player")
        if response:
            self._raw = response
