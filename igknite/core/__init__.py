# Initialize scripts.
from dataclasses import dataclass
from datetime import datetime

from . import chain as chain
from . import datacls as datacls
from .bot import *  # noqa: F403
from .ui import *  # noqa: F403


# Set bot metadata.
@dataclass(frozen=True)
class BotData:
    """
    A dataclass used for storing bot metadata.
    """

    repo: str = 'https://github.com/hitblast/IgKnite'
    running_since: int = round(datetime.timestamp(datetime.now()))
