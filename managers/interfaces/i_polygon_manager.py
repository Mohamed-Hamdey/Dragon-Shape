from abc import ABC, abstractmethod


class PolygonManagerInterface(ABC):
    """Interface for managing polygons."""

    @abstractmethod
    def get_polygons(self):
        """Returns a list of polygons."""
        pass
