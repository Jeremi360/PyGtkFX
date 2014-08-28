
from gi.repository import Gtk
import grabbo

TBui = grabbo.ui.TAB_UI  #os.path.join('..', 'ui', 'TabButton.ui')

class TabButton(grabbo.Builder):
    def __init__(self):
        super(TabButton, self).__init__(TBui)
        self.button = self.ui.get_object("TabButton")
        self.close = self.ui.get_object("Close")

        self.close.connect("clicked", lambda x: self.on_close())
        self.button.connect("clicked", lambda x: self.on_button())

    def set(self, notebook, num, label, closeable = True):
        self.set_closeable(closeable)
        self.button.set_label(label)
        self.notebook = notebook
        self.num = num

    def get(self):
        return self.ui.get_object("box")

    def set_closeable(self,  closeable = True):
        if not closeable:
            self.close.hide()
        else:
            self.close.show()

    def on_button(self):
        self.notebook.pages.set_current_page(self.num)

    def on_close(self):
        self.notebook.pages.prev_page()
        self.notebook.pages.remove_page(self.num)
        self.notebook.buttons_box.remove(self.get())

Nbui = grabbo.ui.NOTEBOOK_UI

class Notebook(grabbo.Builder): #os.path.join("..", "ui", "notebook.ui")
    def __init__(self, addable = True, closeable = True, orientation = Gtk.Orientation.HORIZONTAL):
        super(Notebook, self).__init__(Nubi)

        self.pages = Gtk.Notebook()
        self.set_addable(addable)
        self.set_orientation(orientation)
        self.pages.set_show_tabs(False)
        self.add_button.connect("clicked", lambda x: self.add_tab())
        self.show_all()

    def add_tab(self, content, bt = TabButton(), closeable = True):
        self.pages.append_page(content)
        n = self.pages.page_num(content)

        bt.notebook = self
        bt.num = n
        bt.set_closeable(closeable)
        content.show()

        self.ButtonBox.add(bt.get())

    def get(self):
        return self.ui.get_object("box2")

    def set_addable(self, addable):
        if not addable:
            self.add_button.hide()

    def set_orientation(self, orientation):
            self.ButtonBox.set_orientation(orientation)

            if orientation == Gtk.Orientation.VERTICAL:
                self.ButtonBox.hide()
                self.hide()
                self.set_hexpand(False)
                self.set_vexpand(True)
                self.ButtonBox.set_hexpand(False)
                self.ButtonBox.set_vexpand(True)
                self.ButtonBox.show()

            else:
                self.ButtonBox.hide()
                self.hide()
                self.set_hexpand(True)
                self.set_vexpand(False)
                self.ButtonBox.set_hexpand(True)
                self.ButtonBox.set_vexpand(False)
                self.ButtonBox.show()
