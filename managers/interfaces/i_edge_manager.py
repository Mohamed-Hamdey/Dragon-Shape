from abc import ABC, abstractmethod


class EdgeManagerInterface(ABC):
    """Interface for managing edges."""

    @abstractmethod
    def get_edges(self):
        """Fetches all edges."""
        pass
