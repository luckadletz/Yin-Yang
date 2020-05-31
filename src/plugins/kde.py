import subprocess
from src import config
from src import plugin

class Plugin(plugin.Base):
    @staticmethod
    def name() -> str:
        return "KDE Plasma"
    
    @classmethod
    def apply_light(cls, config):
        super(Plugin, cls).apply_light(config)
        kde_theme = config.get("kdeLightTheme")
        subprocess.run(["lookandfeeltool", "-a", kde_theme])

    @classmethod
    def apply_dark(cls, config):
        super(Plugin, cls).apply_dark(config)
        kde_theme = config.get("kdeDarkTheme")
        subprocess.run(["lookandfeeltool", "-a", kde_theme])

    @classmethod
    def is_enabled(cls, config) -> bool:
        return config.get("kdeEnabled")