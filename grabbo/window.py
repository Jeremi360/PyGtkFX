from gi.repository import Gtk

from grabbo import Builder

class Window(Builder, Gtk.Window):
    def __init__(self, content = Gtk.Box()):
        Gtk.Window.__init__(self)
        self.content = content
        self.do_then_init()

        self.set_size_request(800, 600)
        self.connect("destroy", Gtk.main_quit)
        self.add(self.content)
        self.maximize()

    def do_then_init(self):
        pass
