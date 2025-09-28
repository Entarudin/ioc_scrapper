from enum import Enum


class ScrapperRequestStatus(Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    BROKEN = "broken"
