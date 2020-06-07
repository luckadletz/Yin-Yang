import subprocess
import pwd
import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QFileDialog
from src.ui.mainwindow import Ui_MainWindow
from src.ui.settings import Ui_MainWindow as Ui_SettingsWindow
from src import yin_yang
from src import plugin
from src import config

class SettingsWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)
        # center the settingswindow
        self.center()
        # syncing with config - fill out all fields based on Config
        self.sync_with_config()
        # register all the handler onClick functions ...
        self.register_handlers()

    def register_handlers(self):
        self.ui.back_button.clicked.connect(self.save_and_exit)
        self.ui.apply_button.clicked.connect(self.save)
        self.ui.cancel_button.clicked.connect(self.cancel)
        
        # TODO Disabled defaults - currently saves instantly, overwriting settings on disk
        self.ui.default_button.setEnabled(False)
        # self.ui.default_button.clicked.connect(self.get_defaults)

    # On window close
    def close_event(self, event):
        self.save_and_exit()

    def cancel(self):
        # showing the main window and hiding the current one
        self.hide()
        self.window = MainWindow()
        self.window.show()

    def save(self):
        print("saving options")
        for p in plugin.All():
            try:
                p.update_config(self.ui, config)
            except Exception as ex:
                print(f"error in {p.name()}->update_config!\n{str(ex)}")

    def save_and_exit(self):
        self.save()        
        self.cancel()

    def get_defaults(self):
        config.get_default_config()
        self.sync_with_config()

    def sync_with_config(self):
        # sync config label with get the correct version
        self.ui.version_label.setText("yin-yang: v" + config.get("version"))

        for p in plugin.All():
            try:
                p.update_ui(self.ui, config)
            except Exception as ex:
                print(f"error in {p.name()}->update_ui!\n{str(ex)}")
            
    def center(self):
        frame_gm = self.frameGeometry()
        center_point = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame_gm.moveCenter(center_point)
        self.move(frame_gm.topLeft())


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Yin-Yang")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.center()
        self.register_handlers()
        self.sync_with_config()

    def center(self):
        frame_gm = self.frameGeometry()
        center_point = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame_gm.moveCenter(center_point)
        self.move(frame_gm.topLeft())

    def register_handlers(self):
        # connect the "light" button
        self.ui.light_push.clicked.connect(self.toggle_light)
        # connect the "dark" button
        self.ui.dark_push.clicked.connect(self.toggle_dark)
        # connect the settingsButton
        self.ui.settings_push.clicked.connect(self.open_settings)
        # connect the time change with the correct function
        self.ui.light_time.timeChanged.connect(self.time_changed)
        self.ui.dark_time.timeChanged.connect(self.time_changed)
        self.ui.schedule_radio.toggled.connect(self.toggle_schedule_cliked)

    def sync_with_config(self):
        # sets the scheduled button to be enabled or disabled
        # if config.is_scheduled():
        self.ui.schedule_radio.setChecked(False)
        # sets the correct time based on config
        self.set_correct_time()
        # setting the correct buttons based on config "dark" "light"
        self.set_correct_buttons()

    def open_settings(self):
        self.secwindow = SettingsWindow()
        self.secwindow.setWindowTitle("Settings")
        self.secwindow.show()
        self.hide()

    def toggle_light(self):
        yin_yang.switch_to_light()
        self.sync_with_config()

    def toggle_dark(self):
        yin_yang.switch_to_dark()
        self.sync_with_config()

    def set_correct_time(self):
        new_config = config.get_config()
        d_hour = new_config["switchToDark"].split(":")[0]
        d_minute = new_config["switchToDark"].split(":")[1]
        l_hour = new_config["switchToLight"].split(":")[0]
        l_minute = new_config["switchToLight"].split(":")[1]

        # giving the time widget the values of the config
        dark_time = QTime(int(d_hour), int(d_minute))
        light_time = QTime(int(l_hour), int(l_minute))
        self.ui.dark_time.setTime(dark_time)
        self.ui.light_time.setTime(light_time)

    def set_correct_buttons(self):
        self.ui.light_push.setEnabled(True)
        self.ui.dark_push.setEnabled(True)

    def time_changed(self):
        # update config if time has changed
        l_hour, l_minute = str(self.ui.light_time.time().hour()), str(
            self.ui.light_time.time().minute())
        d_hour, d_minute = str(self.ui.dark_time.time().hour()), str(
            self.ui.dark_time.time().minute())
        config.update("switchToLight", l_hour + ":" + l_minute)
        config.update("switchToDark", d_hour + ":" + d_minute)

    def toggle_schedule_cliked(self):
        checked = self.ui.schedule_radio.isChecked()
        config.update("schedule", checked)
        if checked:
            self.ui.dark_time.setEnabled(True)
            self.ui.light_time.setEnabled(True)
        else:
            self.ui.dark_time.setEnabled(False)
            self.ui.light_time.setEnabled(False)

