import sys

if not sys.executable:
    sys.executable = None

from .__about__ import __version__
from .neo4j import Neo4jCheck

__all__ = ['__version__', 'Neo4jCheck']
