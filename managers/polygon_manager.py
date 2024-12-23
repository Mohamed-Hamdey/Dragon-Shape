from .interfaces.i_polygon_manager import PolygonManagerInterface

class PolygonManager(PolygonManagerInterface):
    """Manages polygons for rendering."""

    def __init__(self, polygons):
        self.polygons = polygons

    def get_polygons(self):
        """Returns the list of polygons."""
        return self.polygons
