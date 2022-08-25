from .__version__ import (
  __author__,
  __author_email__,
  __copyright__,
  __description__,
  __license__,
  __title__,
  __version__
)

import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())