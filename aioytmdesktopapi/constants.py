from enum import Enum


class LikeStatus(str, Enum):
    DISLIKE = "DISLIKE"
    INDIFFERENT = "INDIFFERENT"
    LIKE = "LIKE"


class RepeatType(str, Enum):
    NONE = "NONE"
    ONE = "ONE"
    ALL = "ALL"
