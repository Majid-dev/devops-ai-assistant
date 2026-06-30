from enum import Enum


class Role(str, Enum):
    """
    Supported chat message roles.
    """

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"