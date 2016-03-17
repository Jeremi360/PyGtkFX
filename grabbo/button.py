from gi.repository import Gtk


class StandardButton(Gtk.Button):
    def __init__(self, label = "Button", img = Gtk.Image().new_from_icon_name("dialog-information", 4)):
        Gtk.Button.__init__(self)
        self.set_label(label)
        self.set_relief(Gtk.ReliefStyle.NONE)
        self.set_image(img)

class HomeButton(StandardButton):
    def __init__(self, label):
        img = Gtk.Image().new_from_icon_name("go-home", 4)
        StandardButton.__init__(self, label, img)

class AboutButton(StandardButton):
    def __init__(self):
        img = Gtk.Image().new_from_icon_name("dialog-information", 4)
        StandardButton.__init__(self, "About", img)

class BigLabelButton(StandardButton):
    def __init__(self, label, size = 1):
        l = Gtk.Label()
        s = self._start_size(size)
        m = "<b>" + label + "</b>"
        e = self._end_size(size)
        m = s + m + e
        l.set_markup(m)
        StandardButton.__init__(self, "", l)

    def _start_size(self, size):
        s = ""
        for i in range(size):
            s = s + "<big>"

        return s

    def _end_size(self, size):
        s = ""
        for i in range(size):
            s = s + "</big>"
        return s
