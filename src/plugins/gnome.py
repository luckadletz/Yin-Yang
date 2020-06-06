import subprocess
from src import config

# WIP: Potential Check  for https://gist.github.com/atiensivu/fcc3183e9a6fd74ec1a283e3b9ad05f0 to reduce common issues, or write it in the FAQ
from src import plugin

class Plugin(plugin.Base):
    @staticmethod
    def name() -> str:
        return "Atom"
    
    @classmethod
    def apply_light(cls, config):
        super(Plugin, cls).apply_light(config)
        gnome_theme = config.get("gnomeLightTheme")
        subprocess.run(["gsettings", "set", "org.gnome.shell.extensions.user-theme", "name", '"{}"'.format(gnome_theme)]) # Shell theme

    @classmethod
    def apply_dark(cls, config):
        super(Plugin, cls).apply_dark(config)
        gnome_theme = config.get("gnomeDarkTheme")
        subprocess.run(["gsettings", "set", "org.gnome.shell.extensions.user-theme", "name", '"{}"'.format(gnome_theme)]) # Shell theme

    @classmethod
    def is_enabled(cls, config) -> bool:
        return config.get("gnomeEnabled")

    @classmethod
    def init_config(cls, config):
        config["gnomeEnabled"] = False
        config["gnomeLightTheme"] = ""
        config["gnomeDarkTheme"] = ""
