from src import config
from src import plugin

import os
import pwd

class Plugin(plugin.Base):
    @staticmethod
    def name() -> str:
        return "Kvantum"
    
    @classmethod
    def apply_light(cls, config):
        super(Plugin, cls).apply_light(config)
        kv_theme = config.get("KvantumLightTheme")
        if(kv_theme):
            set_kvantum_theme(kv_theme)

    @classmethod
    def apply_dark(cls, config):
        super(Plugin, cls).apply_dark(config)
        kv_theme = config.get("KvantumDarkTheme")
        if(kv_theme):
            set_kvantum_theme(kv_theme)

    @classmethod
    def is_enabled(cls, config) -> bool:
        return config.get("KvantumEnabled")

def set_kvantum_theme(theme):
    kv_conf_location = get_kvantum_config()
    # Replace theme=* w/ theme=target
    plugin.replace(kv_conf_location, r"^theme\=.*$", f"theme={theme}")
        

def get_kvantum_config():
    user = pwd.getpwuid(os.getuid())[0]
    path = "/home/"+user+"/.config/Kvantum/kvantum.kvconfig"
    return path