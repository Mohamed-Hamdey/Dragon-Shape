from .interfaces.i_translation_manager import TranslationManagerInterface


class TranslationManager(TranslationManagerInterface):
    """Handles translation transformations."""

    def apply_translation(self, vertices, dx, dy):
        return {key: (x + dx, y + dy) for key, (x, y) in vertices.items()}
