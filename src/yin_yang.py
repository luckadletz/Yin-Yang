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
from src.plugins import kde, gtkkde, wallpaper, vscode, atom, gtk, firefox, gnome
from src import config

# aliases for path to use later on
user = pwd.getpwuid(os.getuid())[0]
path = "/home/"+user+"/.config/"

terminate = False


# TODO Poetic, but these should be one class
class Yang(threading.Thread):
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.thread_id = thread_id

    def run(self):
        # TODO loop through enabled plugins dynamically
        if config.get("codeEnabled"):
            vscode.switch_to_light()
        if config.get("atomEnabled"):
            atom.switch_to_light()
        if config.get("kdeEnabled"):
            kde.switch_to_light()
        if config.get("wallpaperEnabled"):
            wallpaper.switch_to_light()
        if config.get("gtkEnabled") and config.get("desktop") == "kde":
            gtkkde.switch_to_light()
        if config.get("gtkEnabled") and config.get("desktop") == "gtk":
            gtk.switch_to_light()
        if config.get("gnomeEnabled"):
            gnome.switch_to_light()
        if config.get("firefoxEnabled"):
            firefox.switch_to_light()
        # play_sound("./assets/light.wav")

class Yin(threading.Thread):
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.thread_id = thread_id

    def run(self):
        if config.get("codeEnabled"):
            vscode.switch_to_dark()
        if config.get("atomEnabled"):
            atom.switch_to_dark()
        if config.get("kdeEnabled"):
            kde.switch_to_dark()
        if config.get("wallpaperEnabled"):
            wallpaper.switch_to_dark()
        # kde support
        if config.get("gtkEnabled") and config.get("desktop") == "kde":
            gtkkde.switch_to_dark()
        # gnome and budgie support
        if config.get("gtkEnabled") and config.get("desktop") == "gtk":
            gtk.switch_to_dark()
        # gnome-shell
        if config.get("gnomeEnabled"):
            gnome.switch_to_dark()
        # firefox support
        if config.get("firefoxEnabled"):
            firefox.switch_to_dark()
        # play_sound("/assets/dark.wav")


class Daemon(threading.Thread):
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.thread_id = thread_id

    def run(self):
        while True:

            if terminate:
                config.update("running", False)
                break

            if not config.is_scheduled():
                config.update("running", False)
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


def switch_to_light():
    yang = Yang(1)
    yang.start()
    config.update("theme", "light")
    yang.join()

def switch_to_dark():
    yin = Yin(2)
    yin.start()
    config.update("theme", "dark")
    yin.join()

def start_daemon():
    daemon = Daemon(3)
    daemon.start()

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
