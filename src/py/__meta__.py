from __future__ import annotations

import importlib.metadata

__version__ = importlib.metadata.version(__package__)
__author__ = importlib.metadata.metadata(__package__)["Author"]
