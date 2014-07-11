from gi.repository import Gtk
from grabbo import Builder

class Window(Builder, Gtk.Window):
    def __init__(self, content = Gtk.Box()):
        Gtk.Window.__init__(self)
        self.set_size_request(400, 400)
        self.connect("destroy", Gtk.main_quit)
        self.maximize()
