# versioneer
from ._version import get_versions
__version__ = get_versions()["version"]
__commit__ = get_versions()["full-revisionid"]
__dirty__ = get_versions()["dirty"]
del get_versions

__url__ = 'https://github.com/humm/scicfg'


# intra-package imports
from .configs import SciConfig
from .types import string
