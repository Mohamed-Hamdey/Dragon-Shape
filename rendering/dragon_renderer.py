from managers import ThemeManager
from .interfaces.i_renderer import RendererInterface
from OpenGL.GL import (
    glBegin,
    glEnd,
    glVertex2fv,
    glColor3f,
    glLineWidth,
    GL_LINES,
    GL_POLYGON,
)

class DragonRenderer(RendererInterface):
    """Handles rendering of the dragon shape."""
    def __init__(self, vertex_manager, edge_manager,
                 polygon_manager=None, color_manager=None,  theme_manager=None):
        self.vertex_manager = vertex_manager
        self.edge_manager = edge_manager
        self.polygon_manager = polygon_manager
        self.color_manager = color_manager
        self.theme_manager = theme_manager or ThemeManager()
        self.is_colored_mode = polygon_manager is not None and color_manager is not None

    def draw(self):
        """Draws the dragon."""
        if self.is_colored_mode:
            self._draw_colored()
        self._draw_edges()

    def _draw_edges(self):
        """Draws the dragon."""
        edge_color = self.theme_manager.edge_color
        glColor3f(*edge_color)
        glLineWidth(2)
        glBegin(GL_LINES)
        for edge in self.edge_manager.get_edges():
            for vertex in edge:
                glVertex2fv(self.vertex_manager.get_vertex_coordinates(vertex))
        glEnd()

    def _draw_colored(self):
        """Draws the colored polygons of the dragon."""
        polygons = self.polygon_manager.get_polygons()
        colors = self.color_manager.get_colors()

        for polygon, color in zip(polygons, colors):
            glColor3f(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0)  # Normalize RGB
            glBegin(GL_POLYGON)
            for vertex in polygon:
                glVertex2fv(self.vertex_manager.get_vertex_coordinates(vertex))
            glEnd()