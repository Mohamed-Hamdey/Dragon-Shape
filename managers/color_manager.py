from .interfaces.i_color_manager import ColorManagerInterface

class ColorManager(ColorManagerInterface):
    """Manages colors for rendering."""

    def __init__(self, colors):
        self.colors = colors

    def get_colors(self):
        """Returns the list of colors."""
        return self.colors
