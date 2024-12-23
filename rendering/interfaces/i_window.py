from abc import ABC, abstractmethod

class WindowInterface(ABC):
    """Interface for OpenGL windows."""

    @abstractmethod
    def setup(self):
        """Sets up the window."""
        pass

    @abstractmethod
    def display_mode_selection(self):
        """Displays buttons for selecting rendering mode."""
        pass

    @abstractmethod
    def run(self, render_function, on_start=None):
        """Runs the main loop with optional on_start callback."""
        pass

    @property
    @abstractmethod
    def mode(self):
        """Gets the current rendering mode."""
        pass

    @mode.setter
    @abstractmethod
    def mode(self, value):
        """Sets the current rendering mode."""
        pass

    def prompt_translation(self):
        """Prompts the user for translation input."""
        pass
