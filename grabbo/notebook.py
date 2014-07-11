
from gi.repository import Gtk
import grabbo
import os

tbui = os.path.join('..', 'ui', 'TabButton.ui')

class _TabButton(grabbo.Builder):
    def __init__(self, title, closeable = True):
        super(_TabButton, self).__init__(tbui)
        self.button = self.ui.get_object("TabButton")
        self.close = self.ui.get_object("close")

        self.set_closeable(closeable)
        self.button.set_label(title)

        self.close.connect("clicked", self.on_close)
        self.button.connect("toggled", self.on_button)

    def set_closeable(self,  closeable = True):
        if not closeable:
            self.close.hide()
        else:
            self.close.show()

    def on_button(self, button, name):
        pass

    def on_close(self, button, name):
        pass

class Notebook(object):
    def __init__(self, addable = True, closeable = True, orientation = Gtk.Orientation.HORIZONTAL):
        self.tabs = Gtk.Notebook()
        self.buttons_box = Gtk.Box()

        self.set_addable(addable)
        self.tabs.set_show_tabs(False)
        self.set_orientation(orientation)

    def set_addable(self, addable):
        if addable:
            self.add_button = Gtk.Button(None)
            self.add_button.new_from_icon_name("gtk-add", 4)
            self.buttons_box.pack_end(self.add_button, False, True, True)

    def set_orientation(self, orientation):
            self.buttons_box.set_orientation(orientation)

            if orientation == Gtk.Orientation.VERTICAL:
                self.buttons_box.set_hexpand(False)
                self.buttons_box.set_vexpand(True)

            else:
                self.buttons_box.set_hexpand(True)
                self.buttons_box.set_vexpand(False)

    def add_tab(self, label = "tab", content = Gtk.Label("Content"), closeable = True):
        print(label)
        self.tabs.append_page(label, content)
        n = self.tabs.page_num(content)

        class temp(_TabButton):
            def __init__(self):
                super(temp, self).__init__(label, closeable)

            def on_button(self, button, name):
                if button.get_active():
                    self.tabs.set_current_page(n)
                else:
                    self.tabs.prev_page()

            def on_close(self, button, name):
                self.tabs.remove_page(n)
                del self

        self.buttons_box.pack_start(temp(), False, True, True)

class Window(grabbo.Window):
    def __init__(self):
        super(Window, self).__init__()

    def do_then_init(self):
        self.content = Gtk.HBox()
        N = Notebook()
        N.add_tab("Test")
        self.content.pack_start(N.buttons_box, False, True, True)
        self.content.pack_end(N.tabs, False, True, True)

if __name__ == "__main__":
    app = Window()
    Gtk.main()
