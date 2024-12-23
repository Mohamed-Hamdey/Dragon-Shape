from .interfaces.i_edge_manager import EdgeManagerInterface

class EdgeManager(EdgeManagerInterface):
    """Handles edges connecting vertices."""
    def __init__(self, edges):
        self.edges = edges

    def get_edges(self):
        return self.edges
