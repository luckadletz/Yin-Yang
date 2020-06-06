import pwd
import os
import re
from src import config
from src import plugin

class Plugin(plugin.Base):
    @staticmethod
    def name() -> str:
        return "KDE/GTK"
    
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
        return config.get("gtkEnabled")

    @classmethod
    def init_config(cls, config):
        # TODO
        pass

    @classmethod
    def update_ui(cls, ui, config):
        # TODO
        pass

    @classmethod
    def update_config(cls, ui, config):
        # TODO
        pass    



# aliases for path to use later on
user = pwd.getpwuid(os.getuid())[0]
path = "/home/"+user+"/.config"


def inplace_change(filename, old_string, new_string):
    """@params: config - config to be written into file
               path - the path where the config is will be written into
                defaults to the default path

    """
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print('"{old_string}" not found in {filename}.'.format(**locals()))
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        print(
            'Changing "{old_string}" to "{new_string}" in {filename}'
            .format(**locals()))
        s = s.replace(old_string, new_string)
        f.write(s)


def switch_to_light():
    gtk_theme = config.get_gtk_light_theme()
    gtk_path = path + "/gtk-3.0"
    with open(gtk_path+"/settings.ini", "r") as file:
        # search for the theme section and change it
        current_theme = re.findall(
            "gtk-theme-name=[A-z -]*", str(file.readlines()))[0][:-2]
        inplace_change(gtk_path+"/settings.ini",
                       current_theme, "gtk-theme-name="+gtk_theme)


def switch_to_dark():
    gtk_theme = config.get_gtk_dark_theme()
    gtk_path = path + "/gtk-3.0"
    with open(gtk_path+"/settings.ini", "r") as file:
        # search for the theme section and change it
        current_theme = re.findall(
            "gtk-theme-name=[A-z -]*", str(file.readlines()))[0][:-2]
        inplace_change(gtk_path+"/settings.ini",
                       current_theme, "gtk-theme-name="+gtk_theme)
