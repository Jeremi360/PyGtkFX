from gi.repository import Gtk
import os
import grabbo

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

TB_UI = os.path.join(r, 'ui', 'TabButton.xml')

class TabButton(grabbo.Builder):
    def __init__(self, notebook, content):
        super(TabButton, self).__init__(TB_UI)
        self.close = self.ui.get_object("CloseButton")
        self.button = self.ui.get_object("TabButton")

        self.close.connect("clicked", self.on_close)
        self.button.connect("clicked", self.on_button)

        self.n = notebook
        self.c = content

    def get(self):
        return self.ui.get_object("box")

    def on_button(self, button):
        self.n.stack.set_visible_child(self.c)

    def on_close(self, button):
        self.n.stack.remove(self.c)
        self.n.switcher.remove(self.get())


NOTEBOOK_UI = os.path.join(r, 'ui', 'Tabs.xml')

class Notebook(grabbo.Builder):
    def __init__(self, stack = Gtk.Stack(), addable = True, closeable = True, orientation = Gtk.Orientation.HORIZONTAL):
        super(Notebook, self).__init__(NOTEBOOK_UI)

        self._sc = self.ui.get_object("scroll")
        self._vp = self.ui.get_object("viewport")
        self.AddButton = self.ui.get_object("AddButton")

        self.get().set_orientation(orientation)
        self.stack = stack
        self.AddButton.connect("clicked", self.on_add)

        self.switcher = Gtk.StackSwitcher()
        self.switcher.set_stack(self.stack)

        self.set_addable(addable)
        self._vp.add(self.switcher)
        self._sc.show_all()
        self.get().show()

    def get(self):
        return self.ui.get_object("box")

    def on_add(self, button):
        content = Gtk.Label()
        content.set_label("Content")
        self.add_tab(content)

    def add_tab(self, content,  tb = None, closeable = True):

        self.stack.add(content)

        if not tb:
            tb = TabButton(self, content)

        if closeable:
            tb.close.show()
        else:
            tb.close.hide()

        self.switcher.add(tb)

    def set_addable(self, addable):
        if addable:
            self.AddButton.show()
        else:
            self.AddButton.hide()

