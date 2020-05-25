
from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def name() -> str:
        return "Plugin Base"

    @classmethod
    @abstractmethod
    def apply_light(cls, config):
        print(f"Let there be light {cls.name()}!")

    @classmethod
    @abstractmethod
    def apply_dark(cls, config):
        print(f"The sun sets on {cls.name()}.")

    @classmethod
    @abstractmethod
    def is_enabled(cls, config) -> bool:
        return False

    # TODO Some way of abstracting out Settings, UI elements...

from src.plugins import kde, gtkkde, wallpaper, vscode, atom, gtk, firefox, gnome

class AllPlugins():
    def __init__(self):
        self.plugins = [
            kde.Plugin(),
            gtkkde.Plugin(),
            wallpaper.Plugin(),
            vscode.Plugin(),
            atom.Plugin(),
            gtk.Plugin(),
            firefox.Plugin(),
            gnome.Plugin()
        ]

    def __iter__(self):
        return self.plugins.__iter__()