from abc import ABC, abstractmethod


class TranslationManagerInterface(ABC):
    """Interface for translation management."""

    @abstractmethod
    def apply_translation(self, vertices, dx, dy):
        """Applies translation to the vertices."""
        pass
