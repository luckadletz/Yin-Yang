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