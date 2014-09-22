from gi.repository import Gtk
import os
import grabbo

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

TB_UI = os.path.join(r, 'ui', 'TabButton.xml')

class TabButton(grabbo.Builder):
    def __init__(self, notebook, content, checked = False):

        self.n = notebook
        self.c = content

        super(TabButton, self).__init__(TB_UI)
        self.close = self.ui.get_object("CloseButton")
        self.button = self.ui.get_object("TabButton")

        self.button.set_active(checked)

        self.close.connect("clicked", self.on_close)
        self.button.connect("toggled", self.on_button)

    def get(self):
        return self.ui.get_object("box")

    def on_button(self, button):
        if self.button.get_active():
            self.n.stack.set_visible_child(self.c)
        else:
            pass

    def on_close(self, button):
        self.n.stack.remove(self.c)
        self.n.switcher.remove(self.get())

class HB_TabButton(TabButton):
    def on_close(self, button):
        grabbo.TabButton.on_close(self, button)
        w = self.n.switcher.get_allocation().width
        self.n.set_width(w)

NOTEBOOK_UI = os.path.join(r, 'ui', 'Notebook.xml')

class Notebook(grabbo.Builder):
    def __init__(self, stack = Gtk.Stack(), addable = True, closeable = True, orientation = Gtk.Orientation.HORIZONTAL):
        super(Notebook, self).__init__(NOTEBOOK_UI)

        self.sc = self.ui.get_object("scrolledwindow1")
        self.vp = self.ui.get_object("viewport1")
        self.AddButton = self.ui.get_object("AddButton")

        self.stack = stack
        self.radiogroup = Gtk.RadioButton()
        self.switcher = Gtk.StackSwitcher()

        self.switcher.add(self.radiogroup)
        self.radiogroup.hide()

        self.switcher.set_stack(self.stack)
        self.get().set_orientation(orientation)
        self.vp.add(self.switcher)

        self.AddButton.connect("clicked", self.on_add)

        self.set_addable(addable)
        self.switcher.show()
        self.get().show()

    def get(self):
        return self.ui.get_object("box1")

    def on_add(self, button):
        content = Gtk.Label()
        content.set_label("Content")
        tb = TabButton(self, content)
        self.add_tab(content, tb)

    def add_tab(self, content, tb, active = False, closeable = True):

        self.stack.add(content)
        self.switcher.add(tb.get())
        self.radiogroup.join_group(tb.button)

        if closeable:
            tb.close.show()
        else:
            tb.close.hide()

        tb.button.set_active(active)

         if active:
            self.stack.set_visible_child(content.get())

    def set_addable(self, addable):
        if addable:
            self.AddButton.show()
        else:
            self.AddButton.hide()

