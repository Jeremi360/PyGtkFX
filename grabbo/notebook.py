
from gi.repository import Gtk
import grabbo
import os

TBui = os.path.join('..', 'ui', 'TabButton.ui')

class TabButton(grabbo.Builder):
    def __init__(self, notebook, num, title, closeable = True):
        super(TabButton, self).__init__(TBui)
        self.button = self.ui.get_object("TabButton")
        self.close = self.ui.get_object("Close")
        self.notebook = notebook
        self.num = num

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
        if self.button.get_active():
            self.notebook.pages.set_current_page(self.num)
        else:
            self.notebook.pages.prev_page()

    def on_close(self):
        self.notebook.pages.remove_page(self.num)
        self.notebook.buttons_box.remove(self.get())
        del self

Nbui = os.path.join("..", "ui", "Notebook.ui")

class Notebook(grabbo.Builder):
    def __init__(self, content = {Gtk.Label("Content"):"Page"}, addable_content = (Gtk.Label("New Content"), "New Page"),
                    addable = True, closeable = True, orientation = Gtk.Orientation.HORIZONTAL):

        super(Notebook, self).__init__(Nbui)
        self.pages = Gtk.Notebook()
        self.buttons_box = self.ui.get_object("ButtonBox")
        self.add_button = self.ui.get_object("Add")

        self.set_addable(addable)
        self.set_orientation(orientation)
        self.pages.set_show_tabs(False)

        for i in content.items():
            self.add_tab(i[0], i[1], closeable)

        if addable:
            self.add_button.connect("clicked", lambda x: self.add_tab(addable_content[0], addable_content[1], closeable))

    def add_tab(self, content = Gtk.Label("Content"), label = None, closeable = True):
        self.pages.append_page(content)
        n = self.pages.page_num(content)

        if label == None:
            label = "Page " + str(n)

        bt = TabButton(self, n, label, closeable)
        content.show()

        self.buttons_box.add(bt.get())

    def get(self):
        return self.ui.get_object("box2")

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
