from gi.repository import Gtk
from grabbo import Window

class HeaderBar(Gtk.HeaderBar):
    def __init__(self):
        Gtk.HeaderBar.__init__(self)
        self.set_show_close_button(True)
        self.set_title("")
        self.props.border_width = 0
        self.props.margin = 0
        self.set_has_subtitle(False)

class tesz(Gtk.Box):
    def __init__(self):
        scroll = Gtk.ScrolledWindow()
        vp = Gtk.Viewport()
        self.box = Gtk.Box()
        self.button = Gtk.Button("add")

        vp.add(self.box)
        scroll.add(vp)

        self.button.connect("clicked", self.on_button)

        self.pack_start(scroll, True, True, True)
        self.pack_end(self.button, True, True, True)

    def on_button(self, button):
        l = Gtk.Label("Test")
        self.box.pack_end(l, True, True, True)


class test(Window):
    def __init__(self):
        super(test, self).__init__()
        hb = HeaderBar()
        box = tesz()
        box.show()
        #hb.pack_start(box)
        self.set_titlebar(hb)
        hb.show()
        self.show()

if __name__ == "__main__":
    app = test()
    Gtk.main()