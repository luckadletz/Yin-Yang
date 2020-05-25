import subprocess
import os
import pwd
from src import config
from src import plugin


class Plugin(plugin.Base):
    @staticmethod
    def name() -> str:
        return "wallpaper"
    
    @classmethod
    def apply_light(cls, config):
        super(Plugin, cls).apply_light(config)
        wallpaper_light = config.get("wallpaperLightTheme")

        if wallpaper_light == "":
            subprocess.run(["notify-send", "looks like no light wallpaper is set"])
        else:
            if config.get("desktop") == "kde":
                subprocess.run(
                    ["sh", "/opt/yin-yang/src/change_wallpaper.sh", wallpaper_light])
            if config.get("desktop") == "gtk":
                subprocess.run(["gsettings", "set", "org.gnome.desktop.background",
                                "picture-uri", "file://"+wallpaper_light])

    @classmethod
    def apply_dark(cls, config):
        super.apply_dark(config)
        wallpaper_dark = config.get("wallpaperDarkTheme")

        if wallpaper_dark == "":
            subprocess.run(["notify-send", "looks like no dark wallpaper is set"])
        else:
            if config.get("desktop") == "kde":
                subprocess.run(
                    ["sh", "/opt/yin-yang/src/change_wallpaper.sh", wallpaper_dark])
            if config.get("desktop") == "gtk":
                subprocess.run(["gsettings", "set", "org.gnome.desktop.background",
                                "picture-uri", "file://"+wallpaper_dark])

    @classmethod
    def is_enabled(cls, config) -> bool:
        return config.get("wallpaperEnabled")

