
from gi.repository import Gtk

class _CloseButton(Gtk.Button):
    def __init__(self, notebook, content):
        super(_CloseButton, self).__init__()
        i = Gtk.Image()
        i.new_from_icon_name("close-window", 4)
        self.set_image(i)
        self.c = content
        self.n = notebook
        self.connect("clicked", self.on_it)

    def on_it(self, button):
        self.n.stack.remove(self.c)
        self.n.switcher.remove(self)

class _TabButton(Gtk.Button):
    def __init__(self, notebook, content):
        super(_TabButton, self).__init__()
        i = Gtk.Image()
        i.new_from_icon_name("applications-internet", 4)
        self.set_image(i)
        self.c = content
        self.n = notebook
        self.connect("clicked", self.on_it)

    def on_it(self, button):
        self.n.set_visible_child(self.c)

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
        sc = Gtk.ScrolledWindow()
        vp.show()
        sc.add(vp)
        sc.show()
        self.pack_start(sc, True, False, 0)
        self.pack_end(self.AddButton, False, False, 0)

    def on_add(self, button):
        content = Gtk.Label()
        content.set_label("Content")
        self.add_tab(content, "Title")

    def add_tab(self, content, title, closeable = True):

        self.stack.add(content)
        box = Gtk.Box()



        if closeable:
            b = _CloseButton(self, content)
            box.pack_end(b, False, False, 0)
            b.show()

        content.show()
        self.switcher.show()


    def set_addable(self, addable):
        if not addable:
            self.AddButton.hide()

