# Initialize scripts.
from dataclasses import dataclass
from datetime import datetime

from . import chain as chain
from . import datacls as datacls
from .bot import *  # noqa: F403
from .ui import *  # noqa: F403

# Set version number.
__version_info__ = ('2025', '2', '28')  # Year.Month.Day
__version__ = '.'.join(__version_info__)


# Set bot metadata.
@dataclass(frozen=True)
class BotData:
    """
    A dataclass used for storing bot metadata.
    """

    repo: str = 'https://github.com/hitblast/IgKnite'
    version: str = __version__
    running_since: int = round(datetime.timestamp(datetime.now()))
