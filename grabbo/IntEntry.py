import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import grabbo

class IntEntry(Gtk.VButtonBox):
    def __init__(self, mini = 0, maxi = None, step = 1):
        Gtk.VButtonBox.__init__(self)
        lay = 5
        self.set_layout(lay)

        expand = False
        fill = False
        padding = 0
        size = 4

        self.mini = mini
        self.maxi = maxi
        self.step = step

        self._AddButton = grabbo.BigLabelButton("+", size)
        self.pack_start(self._AddButton, expand, fill, padding)

        self._Ent = Gtk.Entry()
        purpose = 2
        self._Ent.set_input_purpose(purpose)
        self.set_int(mini)
        self.pack_start(self._Ent, expand, fill, padding)

        self._SubButton = grabbo.BigLabelButton("-", size)

        self.pack_end(self._SubButton, expand, fill, padding)

        self._AddButton.connect("clicked", self.on_add)
        self._SubButton.connect("clicked", self.on_sub)

    def set_max_length(self, length):
        self._Ent.set_max_length(length)
        self.set_int(self.get_int())

    def get_max_length(self, length):
        return self._Ent.get_max_length()

    def set_int(self, fl):
        l = self._Ent.get_max_length()
        l = l - len(str(fl))

        s = ""

        for i in range(l):
            s = s + "0"

        s = s + str(fl)
        self._Ent.set_text(s)

    def get_int(self):
        return int(self._Ent.get_text())

    def add_int(self, fl):
        f = self.get_int()
        f = f + fl
        self.set_int(f)

    def on_add(self, button):
        f = self.get_int()

        try:
            if f < self.maxi:
                self.add_int(self.step)

        except:
            self.add_int(self.step)

    def on_sub(self, button):
        f = self.get_int()

        try:
            if f > self.mini:
                self.add_int(-self.step)

        except:
            self.add_int(-self.step)

if __name__ == '__main__':
    win = grabbo.Window()
    test = IntEntry()
    test.set_max_length(2)
    win.add(test)
    win.show_all()
    Gtk.main()
