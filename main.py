from assets import *

from managers.interfaces import (
    VertexManagerInterface, EdgeManagerInterface,
    ColorManagerInterface, PolygonManagerInterface,
    TranslationManagerInterface, ThemeManagerInterface
)
from managers import (
    VertexManager, EdgeManager,
    ColorManager, PolygonManager,
    TranslationManager, ThemeManager
)
from rendering.interfaces import RendererInterface, WindowInterface
from rendering import OpenGLWindow, DragonRenderer

def main():
    # Instantiate managers
    theme_manager: ThemeManagerInterface = ThemeManager()
    vertex_manager: VertexManagerInterface = VertexManager(vertices)
    edge_manager: EdgeManagerInterface = EdgeManager(edges)
    color_manager: ColorManagerInterface = ColorManager(colors)
    polygon_manager: PolygonManagerInterface = PolygonManager(polygons)
    translation_manager: TranslationManagerInterface = TranslationManager()

    # Setup window and display mode selection
    window: WindowInterface = OpenGLWindow(800, 600, title="Dragon Renderer", theme_manager=theme_manager)
    window.setup()
    window.display_mode_selection()

    # Choose rendering mode based on selection
    renderers = {
        "standard": DragonRenderer(vertex_manager, edge_manager, theme_manager=theme_manager),
        "colored": DragonRenderer(vertex_manager, edge_manager, polygon_manager, color_manager, theme_manager),
    }
    renderer: RendererInterface = renderers.get(window.mode)

    if not renderer:
        print("Invalid mode. Exiting.")
        return

    def translate_and_continue():
        """Handles translation logic after the initial render."""
        nonlocal renderer, vertex_manager
        dx, dy = window.prompt_translation()
        if dx is not None and dy is not None:
            new_vertices = translation_manager.apply_translation(vertices, dx, dy)
            vertex_manager = VertexManager(new_vertices)
            renderer = DragonRenderer(vertex_manager, edge_manager,
                                      polygon_manager, color_manager, theme_manager)
        # Continue rendering with the updated renderer
        window.run(renderer.draw, on_start=None)

    # Start the initial rendering loop with a callback for translation
    window.run(renderer.draw, on_start=translate_and_continue)

if __name__ == "__main__":
    main()
