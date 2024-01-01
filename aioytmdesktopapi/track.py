from .helpers import generate_attribute_string

class Track:
    """Represent Track state."""

    def __init__(self, raw, request) -> None:
        self._raw = raw
        self._request = request

    def __str__(self) -> str:
        attributes = [
            "author",
            "title",
            "album",
            "cover",
            "duration",
            "duration_human",
            "url",
            "id",
            "is_video",
            "is_advertisement",
            "in_library",
        ]
        return generate_attribute_string(self, attributes)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Track):
            return NotImplemented
        return self._raw == other._raw

    @property
    def author(self) -> str:
        return self._raw["author"]

    @property
    def title(self) -> str:
        return self._raw["title"]

    @property
    def album(self) -> str:
        return self._raw["album"]

    @property
    def cover(self) -> str:
        return self._raw["cover"]

    @property
    def duration(self) -> int:
        return self._raw["duration"]

    @property
    def duration_human(self) -> str:
        return self._raw["durationHuman"]

    @property
    def url(self) -> str:
        return self._raw["url"]

    @property
    def id(self) -> str:
        return self._raw["id"]

    @property
    def is_video(self) -> bool:
        return self._raw["isVideo"]

    @property
    def is_advertisement(self) -> bool:
        return self._raw["isAdvertisement"]

    @property
    def in_library(self) -> bool:
        return self._raw["inLibrary"]

    async def update(self) -> None:
        response = await self._request("get", "/track")
        if response:
            self._raw = response
