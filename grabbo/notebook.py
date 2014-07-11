
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

        self.close.connect("clicked", lambda x: self.on_close())
        self.button.connect("toggled", lambda x: self.on_button())

    def get(self):
        return self.ui.get_object("box")

    def set_closeable(self,  closeable = True):
        if not closeable:
            self.close.hide()
        else:
            self.close.show()

    def on_button(self):
        pass

    def on_close(self):
        pass

Nbui = os.path.join("..", "ui", "Notebook.ui")

class Notebook(grabbo.Builder):
    def __init__(self, addable = True, closeable = True, orientation = Gtk.Orientation.HORIZONTAL):
        super(Notebook, self).__init__(Nbui)
        self.pages = Gtk.Notebook()
        self.buttons_box = self.ui.get_object("ButtonBox")
        self.add_button = self.ui.get_object("Add")

        bt = _TabButton("Label")
        b = Gtk.Button()
        b.show()
        self.pages.append_page(Gtk.Label("Tab"), b)

        self.buttons_box.add(bt.get())

        self.set_addable(addable)
        self.set_orientation(orientation)

        self.pages.show()
        self.get().show()

    def get(self):
        return self.ui.get_object("box2")

    def get_pages(self):
        return self.pages

    def set_addable(self, addable):
        if not addable:
            self.add_button.hide()

    def set_orientation(self, orientation):
            self.buttons_box.set_orientation(orientation)

            if orientation == Gtk.Orientation.VERTICAL:
                self.buttons_box.hide()
                self.get().hide()
                self.get().set_hexpand(False)
                self.get().set_vexpand(True)
                self.buttons_box.set_hexpand(False)
                self.buttons_box.set_vexpand(True)
                self.buttons_box.show()

            else:
                self.buttons_box.hide()
                self.get().hide()
                self.get().set_hexpand(True)
                self.get().set_vexpand(False)
                self.buttons_box.set_hexpand(True)
                self.buttons_box.set_vexpand(False)
                self.buttons_box.show()

class Window(grabbo.Window):
    def __init__(self):
        super(Window, self).__init__()
        Box = Gtk.VBox()
        N = Notebook()
        Box.pack_start(N.get(), False, False, 0)
        Box.pack_end(N.get_pages(), False, False, 0)
        self.add(Box)
        Box.show()
        self.show()

if __name__ == "__main__":
    app = Window()
    Gtk.main()
