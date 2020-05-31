
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

    @classmethod
    @abstractmethod
    def save_settings(cls, config):
        pass

    @classmethod
    @abstractmethod
    def load_settings(cls, config):
        pass

    # TODO Some way of abstracting out UI elements...


'''     UTILS       '''

# https://stackoverflow.com/a/39110/7693688
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
import re

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            regex = re.compile(pattern, re.IGNORECASE)
            for line in old_file:
                new_line = regex.sub(subst, line)
                print(new_line[:-1])
                new_file.write(new_line)
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)
    print(f"Updated {file_path}")

from src.plugins.allplugins import AllPlugins as All
