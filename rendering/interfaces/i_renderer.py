from abc import ABC, abstractmethod


class RendererInterface(ABC):
    """Interface for all renderers."""

    @abstractmethod
    def draw(self):
        """Method to draw objects on the screen."""
        pass
