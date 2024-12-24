from abc import ABC, abstractmethod


class ThemeManagerInterface(ABC):
    """Interface for managing theme."""

    @abstractmethod
    def set_theme(self, theme):
        """Sets the current theme."""
        pass
