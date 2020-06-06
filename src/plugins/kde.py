import subprocess
from src import config
from src import plugin

KDE_DARK = "KdeDarkTheme"
KDE_LIGHT = "KdeLightTheme"

class Plugin(plugin.Base):
    @staticmethod
    def name() -> str:
        return "KDE Plasma"
    
    @classmethod
    def apply_light(cls, config):
        super(Plugin, cls).apply_light(config)
        kde_theme = config.get(KDE_LIGHT)
        subprocess.run(["lookandfeeltool", "-a", kde_theme])

    @classmethod
    def apply_dark(cls, config):
        super(Plugin, cls).apply_dark(config)
        kde_theme = config.get(KDE_DARK)
        subprocess.run(["lookandfeeltool", "-a", kde_theme])

    @classmethod
    def is_enabled(cls, config) -> bool:
        return config.get("kdeEnabled")

    @classmethod
    def init_config(cls, config):
        config["kdeLightTheme"] = "org.kde.breeze.desktop"
        config["kdeDarkTheme"] = "org.kde.breezedark.desktop"
        config["kdeEnabled"] = False

    @classmethod
    def update_ui(cls, ui, config):
        cls.get_kde_themes(ui)

        self.ui.kde_checkbox.setChecked(config.get("kdeEnabled"))
        self.ui.kde_combo_dark.setEnabled(config.get("kdeEnabled"))
        self.ui.kde_combo_light.setEnabled(config.get("kdeEnabled"))
        index_light = self.ui.kde_combo_light.findText(
            self.get_kde_theme_short(config.get("kdeLightTheme")))
        self.ui.kde_combo_light.setCurrentIndex(index_light)
        index_dark = self.ui.kde_combo_dark.findText(
            self.get_kde_theme_short(config.get("kdeDarkTheme")))
        self.ui.kde_combo_dark.setCurrentIndex(index_dark)

    @classmethod
    def update_config(cls, ui, config):
        kde_light_short = self.ui.kde_combo_light.currentText()
        kde_dark_short = self.ui.kde_combo_dark.currentText()

        config.update("kdeLightTheme",
                      self.get_kde_theme_long(kde_light_short))
        config.update("kdeDarkTheme", self.get_kde_theme_long(kde_dark_short))
        config.update("kdeEnabled", self.ui.kde_checkbox.isChecked())

    @classmethod
    def get_kde_themes(cls, ui):
        """
        Sends the kde themes to the ui.
        """
        if config.get("desktop") == "kde":
            if (ui.kde_combo_light.count() == 0 and ui.kde_combo_dark.count() == 0):
                kde_themes = cls.get_kde_theme_names()

                for name, theme in kde_themes.items():
                    ui.kde_combo_light.addItem(name)
                    ui.kde_combo_dark.addItem(name)
        else:
            ui.kde_combo_light.setEnabled(False)
            ui.kde_combo_dark.setEnabled(False)
            ui.kde_checkbox.setChecked(False)
            config.update("codeEnabled", False)

    @classmethod
    def get_kde_theme_names(cls):
        """
        Returns a map with translations for kde theme names.
        """

        # aliases for path to use later on
        user = pwd.getpwuid(os.getuid())[0]
        path = "/home/"+user+"/.local/share/plasma/look-and-feel/"

        # asks the system what themes are available
        long_names = subprocess.check_output(
            ["lookandfeeltool", "-l"], universal_newlines=True)
        long_names = long_names.splitlines()

        themes = {}

        # get the actual name
        for long in long_names:
            # trying to get the Desktop file
            try:
                # load the name from the metadata.desktop file
                with open('/usr/share/plasma/look-and-feel/{long}/metadata.desktop'.format(**locals()), 'r') as file:
                    # search for the name
                    for line in file:
                        if 'Name=' in line:
                            name: str = ''
                            write: bool = False
                            for letter in line:
                                if letter == '\n':
                                    write = False
                                if write:
                                    name += letter
                                if letter == '=':
                                    write = True
                            themes[name] = long
                            break
            except:
                # check the next path if the themes exist there
                try:
                    # load the name from the metadata.desktop file
                    with open('{path}{long}/metadata.desktop'.format(**locals()), 'r') as file:
                        # search for the name
                        for line in file:
                            if 'Name=' in line:
                                name: str = ''
                                write: bool = False
                                for letter in line:
                                    if letter == '\n':
                                        write = False
                                    if write:
                                        name += letter
                                    if letter == '=':
                                        write = True
                                themes[name] = long
                                break
                        # if no file exist lets just use the long name
                except:
                    themes[long] = long

        return themes

    def get_kde_theme_long(self, short: str):
        """
        Translates short names to long names.
        :param short: short name
        :return: long name
        """
        if short == '' or short is None:
            return
        themes = self.get_kde_theme_names()
        return themes[short]

    def get_kde_theme_short(self, long: str):
        """
        Translates long names to short names.
        :param long: long name
        :return: short name
        """
        if long == '' or long is None:
            return
        themes = self.get_kde_theme_names()
        short_names = list(themes.keys())
        long_names = list(themes.values())
        return short_names[long_names.index(long)]