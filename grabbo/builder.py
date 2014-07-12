from gi.repository import Gtk

class Builder(object):
    def __init__(self, UI_FILE):
        #load UI from UI_FILE
        self.ui = Gtk.Builder()

        try:
            self.ui.add_from_file(UI_FILE)
        except:
            self.ui.add_from_string(UI_FILE)

        self.ui.connect_signals(self)
