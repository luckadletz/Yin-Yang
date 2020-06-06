import subprocess
from src import config
from src import plugin

class Plugin(plugin.Base):
    @staticmethod
    def name() -> str:
        return "Atom"
    
    @classmethod
    def apply_light(cls, config):
        super(Plugin, cls).apply_light(config)
        switch_to_light(config)

    @classmethod
    def apply_dark(cls, config):
        super(Plugin, cls).apply_dark(config)
        switch_to_dark(config)

    @classmethod
    def is_enabled(cls, config) -> bool:
        return config.get("atomEnabled")

    @classmethod
    def init_config(cls, config):
        config["gtkLightTheme"] = ""
        config["gtkDarkTheme"] = ""
        config["gtkEnabled"] = False

    @classmethod
    def update_ui(cls, ui, config):
        self.ui.gtk_line_light.setText(config.get("gtkLightTheme"))
        self.ui.gtk_line_dark.setText(config.get("gtkDarkTheme"))
        self.ui.gtk_checkbox.setChecked(config.get("gtkEnabled"))
        self.ui.gtk_line_light.setEnabled(config.get("gtkEnabled"))
        self.ui.gtk_line_dark.setEnabled(config.get("gtkEnabled"))

    @classmethod
    def update_config(cls, ui, config):
        config.update("gtkLightTheme", self.ui.gtk_line_light.text())
        config.update("gtkDarkTheme", self.ui.gtk_line_dark.text())
        config.update("gtkEnabled", self.ui.gtk_checkbox.isChecked())

def switch_to_light():
    gtk_theme = config.get("gtkLightTheme")
    # gtk_theme = "Default"
    # uses a kde api to switch to a light theme
    subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", gtk_theme]) # Applications theme
    #subprocess.run(["gsettings", "set", "org.gnome.shell.extensions.user-theme", "name", '"{}"'.format(gtk_theme)]) # Shell theme


def switch_to_dark():
    gtk_theme = config.get("gtkDarkTheme")
    # uses a kde api to switch to a dark theme
    subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", gtk_theme]) # Applications theme
    #subprocess.run(["gsettings", "set", "org.gnome.shell.extensions.user-theme", "name", '"{}"'.format(gtk_theme)]) # Shell theme
