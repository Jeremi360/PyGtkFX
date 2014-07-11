
from gi.repository import Gtk
import grabbo
import os

tbui = os.path.join('..', 'ui', 'TabButton.ui')

class _TabButton(grabbo.Builder):
    def __init__(self, title, tab, closeable = True):
        super(_TabButton, self).__init__(tbui)
        self.tab = tab
        self.button = self.ui.get_object("TabButton")
        self.close = self.ui.get_object("close")

        self.set_closeable(closeable)
        self.button.set_label(title)

        self.closefb.connect("clicked", self)


    def set_closeable(self,  closeable = True):
        if not closeable:
            self.close.hide()
        else:
            self.close.show()

    def on_button(self):
        pass

    def on_close(self):
        pass

class Notebook(object):
    def __init__(self, tabs = {"tab":Gtk.Label("Content")}, addable = True, closeable = True, orientation = Gtk.Orientation.HORIZONTAL):
        self.tabs = Gtk.Notebook()
        self.buttons_box = Gtk.Box()

        self.set_addable(addable)
        self.tabs.set_show_tabs(False)
        self.set_orientation(orientation)
        self.add_tabs(tabs, closeable)

    def set_addable(self, addable):
        if addable:
            self.add_button = Gtk.Button(None)
            self.add_button.set_image(Gtk.Image.set_from_icon_name("gtk-add"))
            self.buttons_box.pack_end(self.add_button)

    def set_orientation(self, orientation):
            self.buttons_box.set_orientation(orientation)

            if orientation == Gtk.Orientation.VERTICAL:
                self.buttons_box.set_hexpand(False)
                self.buttons_box.set_vexpand(True)

            else:
                self.buttons_box.set_hexpand(True)
                self.buttons_box.set_vexpand(False)

    def add_tabs(self, tabs = {"tab":Gtk.Label("Content")}, closeable):
        for t in tabs.items():
            self.tabs.append_page(t[0], t[1])
            class temp(_TabButton):

            self.buttons_box.pack_start()

