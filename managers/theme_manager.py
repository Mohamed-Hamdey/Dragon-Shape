from managers.interfaces import ThemeManagerInterface


class ThemeManager(ThemeManagerInterface):
    """Handles theme configurations (e.g., light and dark modes)."""
    def __init__(self, theme="light"):
        self.theme = None
        self.text_color = None
        self.edge_color = None
        self.button_color = None
        self.background_color = None
        self.set_theme(theme)

    def set_theme(self, theme):
        """Sets the current theme."""
        if theme == "dark":
            self.background_color = (0.1, 0.1, 0.1)  # Dark gray
            self.edge_color = (1, 1, 1)  # White edges
            self.button_color = (50, 50, 50)  # Dark gray buttons
            self.text_color = (255, 255, 255)  # White text
        else:
            self.background_color = (1, 1, 1)  # White
            self.edge_color = (0, 0, 0)  # Black edges
            self.button_color = (255, 255, 255)  # White buttons
            self.text_color = (0, 0, 0)  # Black text
        self.theme = theme
