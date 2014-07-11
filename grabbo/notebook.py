
from gi.repository import Gtk
import grabbo
import os

TBui = os.path.join('..', 'ui', 'TabButton.ui')

class _TabButton(grabbo.Builder):
    def __init__(self, title, closeable = True):
        super(_TabButton, self).__init__(TBui)
        self.button = self.ui.get_object("TabButton")
        self.close = self.ui.get_object("Close")

        self.set_closeable(closeable)
        self.button.set_label(title)

        self.close.connect("clicked", self.on_close)
        self.button.connect("toggled", self.on_button)

    def get(self):
        return self.ui.get_object("box")

    def set_closeable(self,  closeable = True):
        if not closeable:
            self.close.hide()
        else:
            self.close.show()

    def on_button(self, button, name):
        pass

    def on_close(self, button, name):
        pass

Nbui = os.path.join("..", "ui", "Notebook.ui")

class Notebook(grabbo.Builder):
    def __init__(self, addable = True, closeable = True, orientation = Gtk.Orientation.HORIZONTAL):
        super(Notebook, self).__init__(Nbui)
        self.notebook = self.ui.get_object('Notebook')
        self.buttons_box = self.ui.get_object("ButtonBox")
        self.add_button = self.ui.get_object("Add")

        self.set_addable(addable)
        self.set_orientation(orientation)

        self.add_button.connet('clicked', self.add_button())

        self.get().show()

    def get(self):
        return self.ui.get_object("box")

    def set_addable(self, addable):
        if not addable:
            self.add_button.hide()

    def set_orientation(self, orientation):
            self.buttons_box.set_orientation(orientation)

            if orientation == Gtk.Orientation.VERTICAL:
                self.buttons_box.hide()
                self.buttons_box.set_hexpand(False)
                self.buttons_box.set_vexpand(True)
                self.buttons_box.show()

            else:
                self.buttons_box.hide()
                self.buttons_box.set_hexpand(True)
                self.buttons_box.set_vexpand(False)
                self.buttons_box.show()

class Window(grabbo.Window):
    def __init__(self):
        super(Window, self).__init__()
        N = Notebook()
        N.tabs.append_page(Gtk.Label("Tab"), Gtk.Label("Content"))
        tb = _TabButton("Tab")
        N.buttons_box.add(tb)
        self.add(N.get())
        self.show()

if __name__ == "__main__":
    app = Window()
    Gtk.main()
