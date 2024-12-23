from managers import ThemeManager
from .interfaces.i_window import WindowInterface
import tkinter as tk
from tkinter import simpledialog, messagebox
import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import (
    glMatrixMode, glLoadIdentity, GL_PROJECTION,
    glClear, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT,
    glClearColor, glViewport
)
from OpenGL.GLU import gluOrtho2D


class OpenGLWindow(WindowInterface):
    """Handles OpenGL window and rendering."""
    def __init__(self, width, height, title="OpenGL Window", theme_manager=None):
        self.screen = None
        self.width = width
        self.height = height
        self.title = title
        self._mode = None  # Rendering mode: "standard" or "colored"
        self.theme_manager = theme_manager or ThemeManager()

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value

    def setup(self):
        """Sets up the OpenGL environment."""
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height), DOUBLEBUF | OPENGL)
        pygame.display.set_caption(self.title)
        self._setup_opengl()

    def display_mode_selection(self):
        """Displays buttons for selecting rendering mode."""
        self._switch_to_pygame_context()
        self._render_buttons([
            {"label": "Standard Mode", "action": "standard"},
            {"label": "Colored Mode", "action": "colored"},
            {"label": "Toggle Theme", "action": "toggle_theme"},
        ])
        self._switch_to_opengl_context()

    def run(self, render_function, on_start=None):
        """Runs the main loop with optional on_start callback."""
        if on_start:
            # Render the shape once before handling the on_start logic
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            render_function()
            pygame.display.flip()
            pygame.time.wait(10)  # Brief pause for visualization
            on_start()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            render_function()
            pygame.display.flip()
            pygame.time.wait(10)

    def _setup_opengl(self):
        """Configures OpenGL settings with the current theme."""
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-15, 15, -10, 10)
        bg_color = self.theme_manager.background_color
        glClearColor(*bg_color, 1)  # Use theme background color

    def _switch_to_pygame_context(self):
        """Switches to Pygame's 2D rendering context."""
        glViewport(0, 0, self.width, self.height)
        self.screen = pygame.display.set_mode((self.width, self.height))

    def _switch_to_opengl_context(self):
        """Switches back to OpenGL rendering context."""
        self.screen = pygame.display.set_mode((self.width, self.height), DOUBLEBUF | OPENGL)
        self._setup_opengl()

    def _render_buttons(self, buttons):
        """Helper to render buttons with theming support."""
        self.screen.fill(self.theme_manager.button_color)  # Clear Pygame screen
        font = pygame.font.SysFont("Arial", 24)

        total_height = len(buttons) * 70  # 50px height + 20px margin
        start_y = (self.height - total_height) // 2

        for idx, button in enumerate(buttons):
            rect = pygame.Rect((self.width - 200) // 2, start_y + idx * 70, 200, 50)
            pygame.draw.rect(self.screen, self.theme_manager.text_color, rect, 2)
            text_surface = font.render(button["label"], True, self.theme_manager.text_color)
            text_rect = text_surface.get_rect(center=rect.center)
            self.screen.blit(text_surface, text_rect)

        pygame.display.flip()

        while self._mode is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = event.pos
                    for idx, button in enumerate(buttons):
                        rect = pygame.Rect((self.width - 200) // 2, start_y + idx * 70, 200, 50)
                        if rect.collidepoint(mouse_pos):
                            if button["action"] == "toggle_theme":
                                self._toggle_theme()
                            else:
                                self._mode = button["action"]

    def _toggle_theme(self):
        """Toggles between light and dark themes."""
        new_theme = "dark" if self.theme_manager.theme == "light" else "light"
        self.theme_manager.set_theme(new_theme)
        self._render_buttons([
            {"label": "Standard Mode", "action": "standard"},
            {"label": "Colored Mode", "action": "colored"},
            {"label": "Toggle Theme", "action": "toggle_theme"},
        ])

    def prompt_translation(self):
        """Prompts the user for translation input."""
        root = tk.Tk()
        root.withdraw()  # Hide the main Tkinter window

        answer = messagebox.askyesno("Translation", "Do you want to translate the shape?")
        if not answer:
            return None, None

        dx = simpledialog.askfloat("Translation Input X", "Enter X translation:")
        dy = simpledialog.askfloat("Translation Input Y", "Enter Y translation:")

        if dx is None or dy is None:
            messagebox.showinfo("Translation", "Translation cancelled.")
            return None, None

        return dx, dy