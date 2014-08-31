from gi.repository import Gtk

r = os.path.realpath(__file__)
LIST_UI = os.path.join(r, '..', 'ui', 'Tabs.xml')

    def on_it(self, button):
        self.n.stack.remove(self.c)
        self.n.switcher.remove(self)

class Notebook(Gtk.Box):
    def __init__(self, stack = Gtk.Stack(), addable = True, closeable = True, orientation = Gtk.Orientation.HORIZONTAL):
        super(Notebook, self).__init__()
        self.set_orientation(orientation)

        img = Gtk.Image()
        img.new_from_icon_name("list-add", 4)
        self.AddButton = Gtk.Button("add")
        self.AddButton.set_image(img)
        self.AddButton.set_always_show_image(True)
        self.AddButton.set_vexpand(False)
        self.AddButton.set_hexpand(False)

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
        self.pack_start(self._sc, False, False, 0)
        self.add(self.AddButton)

    def on_add(self, button):
        content = Gtk.Label()
        content.set_label("Content")
        self.add_tab(content)

    def add_tab(self, content, closeable = True):

        self.stack.add_titled(content, "_Namestack", "LabelInTheSwitcher")

        if closeable:
            cb = _CloseButton(self, content)
            self.switcher.add(cb)
            cb.show()

    def set_addable(self, addable):
        if not addable:
            self.AddButton.hide()

