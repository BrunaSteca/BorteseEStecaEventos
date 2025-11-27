from django.apps import AppConfig


class PaginasConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "paginas"
    verbose_name = "Páginas"

    def ready(self) -> None:
        """Importa signals da app (se existirem) para que sejam registrados ao iniciar."""
        try:
            from . import signals  # noqa: F401
        except ImportError:
            # Módulo signals não existe — comportamento esperado em muitos projetos.
            # Não silenciamos outras exceções para não ocultar erros reais no módulo.
            pass
