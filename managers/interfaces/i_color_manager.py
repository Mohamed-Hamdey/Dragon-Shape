from abc import ABC, abstractmethod


class ColorManagerInterface(ABC):
    """Interface for managing colors."""

    @abstractmethod
    def get_colors(self):
        """Returns a list of colors."""
        pass
