from .interfaces.i_vertex_manager import VertexManagerInterface

class VertexManager(VertexManagerInterface):
    """Handles vertices and their relationships."""
    def __init__(self, vertices):
        self.vertices = vertices

    def get_vertex_coordinates(self, vertex):
        return self.vertices[vertex]
