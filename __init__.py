"""
Auth Toolkit - Flexible authentication module
"""

from .core import Auth, DefaultMethods, JWTBackend, AuthDefaults, merge_defaults
from .exceptions import JWTError
from .plugins.websocket import websocket_auth

__version__ = '0.1.0'

__all__ = [
    'Auth',
    'DefaultMethods',
    'JWTBackend',
    'AuthDefaults',
    'merge_defaults',
    'JWTError',
    'websocket_auth',
]
