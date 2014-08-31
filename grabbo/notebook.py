
from gi.repository import Gtk

class _NButton(Gtk.Button):
    def __init__(self, notebook, content, icon_name):
        super(_NButton, self).__init__()
        i = Gtk.Image()
        i.new_from_icon_name(icon_name, 4)
        self.set_image(i)
        self.c = content
        self.n = notebook
        self.connect("clicked", self.on_it)

    def on_it(self, button):
        pass


class _CloseButton(_NButton):
    def __init__(self, n, c):
        super(_CloseButton, self).__init__(n, c, "close-window")

    def on_it(self, button):
        self.n.stack.remove(self.c)
        self.n.switcher.remove(self)

class Notebook(Gtk.Box):
    def __init__(self, stack = Gtk.Stack(), addable = True, closeable = True, orientation = Gtk.Orientation.HORIZONTAL):
        super(Notebook, self).__init__()
        self.set_orientation(orientation)

        AddIcon = Gtk.Image()
        AddIcon.new_from_icon_name("list-add", 4)

        self.AddButton = Gtk.Button()
        self.AddButton.set_image(AddIcon)

        self.stack = stack

        self.set_addable(addable)
        self.set_orientation(orientation)
        self.AddButton.connect("clicked", self.on_add)

        self.switcher = Gtk.StackSwitcher()
        self.switcher.set_stack(self.stack)

        vp = Gtk.Viewport()
        self.switcher.show()
        vp.add(self.switcher)
        self._sc = Gtk.ScrolledWindow()
        vp.show()
        self._sc.add(vp)
        self._sc.show()
        self.pack_start(self._sc, True, False, 0)
        self.pack_end(self.AddButton, False, False, 0)

    def on_add(self, button):
        content = Gtk.Label()
        content.set_label("Content")
        self.add_tab(content)

    def add_tab(self, content, closeable = True):

        self.stack.add(content)

        if closeable:
            cb = _CloseButton(self, content)
            self.switcher.pack_end(cb, False, False, 0)
            cb.show()

    def set_addable(self, addable):
        if not addable:
            self.AddButton.hide()

