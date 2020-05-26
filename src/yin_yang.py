#!/bin/python

"""
title: yin_yang
description: yin_yang provides a easy way to toggle between light and dark
mode for your kde desktop. It also themes your vscode and
all other qt applications with it.
author: luckadletz, daehruoydeef
date: 5/23/2020
license: MIT
"""

import os
import sys
import threading
import time
import pwd
import datetime
import subprocess

from src import gui
from src import plugin
from src import config

# aliases for path to use later on
user = pwd.getpwuid(os.getuid())[0]
path = "/home/"+user+"/.config/"

terminate = False

class YinYang():
    def __init__(self, config, light):
        self.config = config
        self.light = light

    def run(self):
        self.config.update("theme", "light")
        if(self.light):
            self.apply_all_light()
        else:
            self.apply_all_dark()

    def apply_all_dark(self):
        for p in plugin.AllPlugins():
            if(p.is_enabled(self.config)):
                p.apply_dark(self.config)

    def apply_all_light(self):
        for p in plugin.AllPlugins():
            if(p.is_enabled(self.config)):
                p.apply_light(self.config)

def switch_to_light():
    yin = YinYang(config, True)
    yin.run()

def switch_to_dark():
    yang = YinYang(config, False)
    yang.run()

def toggle_theme():
    theme = config.get_theme()
    if theme == "dark":
        switch_to_light()
    elif theme == "light":
        switch_to_dark()
    else:
        print("No theme has been applied yet. Apply a theme or set a schedule first.")

class Daemon(threading.Thread):
    # TODO it's probably better to just add `yin-yang -L` and `yin-yang -D` to chron than run a python thread...
    '''
    # Appply light themes at 7:30 AM each day
    30 7 * * * /usr/bin/yin-yang -L
    # Appply dark themes at 4:20 PM each day
    20 16 * * * /usr/bin/yin-yang -D
    '''
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.thread_id = thread_id

    def run(self):
        while True:
            if terminate:
                break
            if not config.is_scheduled():
                break
            editable = config.get_config()

            theme = config.get("theme")

            if should_be_light():
                if theme == "light":
                    time.sleep(30)
                    continue
                else:
                    switch_to_light()
            else:
                if theme == "dark":
                    time.sleep(30)
                    continue
                else:
                    switch_to_dark()

            time.sleep(30)

def start_daemon():
    if config.get("followSun"):
        # calculate time if needed
        config.set_sun_time()
    daemon = Daemon(3)
    daemon.start()
    # Wait, doesn't this just loop until the main process is killed?

def should_be_light():
    # desc: return if the Theme should be light
    # returns: True if it should be light
    # returns: False if the theme should be dark

    d_hour = int(config.get("switchToDark").split(":")[0])
    d_minute = int(config.get("switchToDark").split(":")[1])
    l_hour = int(config.get("switchToLight").split(":")[0])
    l_minute = int(config.get("switchToLight").split(":")[1])
    hour = datetime.datetime.now().time().hour
    minute = datetime.datetime.now().time().minute

    # TODO this is strange?
    if(hour >= l_hour and hour < d_hour):
        return not (hour == l_hour and minute <= l_minute)
    else:
        return hour == d_hour and minute <= d_minute
