import sys
from argparse import ArgumentParser
from src import yin_yang
from src import config
from src import gui
from PyQt5 import QtWidgets
from PyQt5 import QtCore

# fix HiDpi scaling
QtWidgets.QApplication.setAttribute(
    QtCore.Qt.AA_EnableHighDpiScaling, True)

def launch_gui():
    print("Launching gui")
    app = QtWidgets.QApplication(sys.argv)
    window = gui.MainWindow()
    window.show()
    sys.exit(app.exec_())

def main():
    # using ArgumentParser for parsing arguments
    parser = ArgumentParser()
    parser.add_argument("-t", "--toggle", help="toggles Yin-Yang",
                        action="store_true")
    parser.add_argument("-D", "--dark", help="Apply all dark themes",
                        action="store_true")
    parser.add_argument("-L", "--light", help="Apply all light themes",
                        action="store_true")
    parser.add_argument("-s", "--schedule", help="schedule theme toggl, starts daemon in bg",
                        action="store_true")
    parser.add_argument("-c", "--config", help="Launch the gui to configure settings",
                        action="store_true")
    args = parser.parse_args()

    if len(sys.argv) <=1 or args.config == True:
        launch_gui()
        return

    if args.toggle == True:
        yin_yang.toggle_theme()
        return

    if args.dark == True and args.light == True:
        print("You must choose.")
        return
    elif args.dark == True:
        yin_yang.switch_to_dark()
        return
    elif args.light == True:
        yin_yang.switch_to_light()
        return

    # checks wether the script should be ran as a daemon
    if args.schedule == True:
        if config.get("schedule"):
            yin_yang.start_daemon()
        else:
            print("looks like you did not specified a time")
            print("You can use the gui with yin-yang -gui")
            print("Or edit the config found in ~/.config/yin_yang/yin_yang.json")
            print("You need to set schedule to True and edit the time to toggle")

    # No args
    parser.print_help()

if __name__ == "__main__":
    main()
