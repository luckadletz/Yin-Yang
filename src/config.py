import json
import pwd
import os
import pathlib
import re
from suntime import Sun, SunTimeException

from src import plugin

# aliases for path to use later on
user = pwd.getpwuid(os.getuid())[0]
path = "/home/"+user+"/.config"


def exists():
    """returns True or False wether Config exists or note"""
    return os.path.isfile(path+"/yin_yang/yin_yang.json")


def get_desktop():
    """Return the current desktop's name or 'unkown' if can't determine it"""
    # just to get all possible implementations of dekstop variables
    env = str(os.getenv("GDMSESSION")).lower()
    second_env = str(os.getenv("XDG_CURRENT_DESKTOP")).lower()
    third_env = str(os.getenv("XDG_CURRENT_DESKTOP")).lower()

    # these are the envs I will look for
    # feel free to add your Desktop and see if it works
    gnome_re = re.compile(r'gnome')
    budgie_re = re.compile(r'budgie')
    kde_re = re.compile(r'kde')
    plasma_re = re.compile(r'plasma')
    plasma5_re = re.compile(r'plasma5')

    if gnome_re.search(env) or gnome_re.search(second_env) or gnome_re.search(third_env):
        return "gtk"
    if budgie_re.search(env) or budgie_re.search(second_env) or budgie_re.search(third_env):
        return "gtk"
    if kde_re.search(env) or kde_re.search(second_env) or kde_re.search(third_env):
        return "kde"
    if plasma_re.search(env) or plasma_re.search(second_env) or plasma_re.search(third_env):
        return "kde"
    if plasma5_re.search(env) or plasma5_re.search(second_env) or plasma5_re.search(third_env):
        return "kde"
    return "unknown"


def set_sun_time():
    latitude: float = float(get("latitude"))
    longitude: float = float(get("latitude"))
    sun = Sun(latitude, longitude)

    try:
        today_sr = sun.get_local_sunrise_time()
        today_ss = sun.get_local_sunset_time()

        print('Today the sun raised at {} and get down at {}'.
              format(today_sr.strftime('%H:%M'), today_ss.strftime('%H:%M')))

        # Get today's sunrise and sunset in UTC
        update("switchToLight", today_sr.strftime('%H:%M'))
        update("switchToDark", today_ss.strftime('%H:%M'))

    except SunTimeException as e:
        print("Error: {0}.".format(e))


# generate path for yin-yang if there is none this will be skipped
pathlib.Path(path+"/yin_yang").mkdir(parents=True, exist_ok=True)


# if there is no config generate a generic one
config = {}
config["version"] = "2.0"
config["desktop"] = get_desktop()
config["followSun"] = False
config["latitude"] = ""
config["longitude"] = ""
config["schedule"] = False
config["switchToDark"] = "20:00"
config["switchToLight"] = "07:00"



if exists():
    # making config global for this module
    with open(path+"/yin_yang/yin_yang.json", "r") as conf:
        config = json.load(conf)

config["desktop"] = get_desktop()

def get_default_config():
    for p in plugin.All():
        try:
            p.set_default_settings(config)
        except Exception as ex:
            print(f"error in {p.name()}->set_default_settings!\n{str(ex)}")

def get_config():
    """returns the config"""
    return config


def update(key, value):
    """Update the value of a key in configuration"""
    config[key] = value
    write_config()

def write_config(config=config):
    """Write configuration"""
    with open(path+"/yin_yang/yin_yang.json", 'w') as conf:
        json.dump(config, conf, indent=4)

def gtk_exists():
    return os.path.isfile(path+"/gtk-3.0/settings.ini")

def get(key):
    try:
        return config[key]
    except:
        print(f"Key: {key} not found in config!")
        return None