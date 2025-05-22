from .base import *


ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8080",
]
INTERNAL_IPS = [
    "127.0.0.1",
]

try:
    from .local_settings import *
except ImportError:
    pass
