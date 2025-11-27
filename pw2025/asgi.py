"""
ASGI config for pw2025 project.

It exposes the ASGI callable as a module-level variable named ``application``.
"""

import os
from typing import Any

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pw2025.settings")

# Obtem a aplicação ASGI padrão do Django (comportamento inalterado)
application: Any = get_asgi_application()
