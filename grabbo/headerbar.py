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

class test(Window):
    def __init__(self):
        super(test, self).__init__()
        hb = HeaderBar()
        scroll = Gtk.ScrolledWindow()
        vp = Gtk.Viewport()
        self.box = Gtk.Box()
        button = Gtk.Button("add")
        box_zwie = Gtk.Box()

        vp.add(self.box)
        scroll.add(vp)

        button.connect("clicked", self.on_button)

        box_zwie.pack_start(scroll, True, True, True)
        box_zwie.pack_end(button, True, True, True)
        hb.pack_start(box_zwie)
        self.set_titlebar(hb)
        hb.show_all()
        self.show()

    def on_button(self, button):
        l = Gtk.Label("Test")
        self.box.pack_end(l, True, True, True)

if __name__ == "__main__":
    app = test()
    Gtk.main()