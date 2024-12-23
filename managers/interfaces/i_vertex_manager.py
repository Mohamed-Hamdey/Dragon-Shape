from abc import ABC, abstractmethod


class VertexManagerInterface(ABC):
    """Interface for managing vertices."""

    @abstractmethod
    def get_vertex_coordinates(self, vertex):
        """Fetches coordinates of a given vertex."""
        pass
