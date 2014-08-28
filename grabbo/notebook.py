
from gi.repository import Gtk

class _CloseButton(Gtk.Button):
    def __init__(self, notebook, content):
        super(_CloseButton, self).__init__()
        i = Gtk.Image()
        i.new_from_icon_name("close-window", 4)
        self.set_image(i)
        self.c = content
        self.n = notebook

    def on_it(self, button):
        self.n.stack.remove(self.c)
        self.switcher.remove(self)


class Notebook(Gtk.Box):
    def __init__(self, AddButtonable = True, closeable = True, orientation = Gtk.Orientation.HORIZONTAL):
        super(Notebook, self).__init__()
        self.set_orientation(Gtk.Orientation.VERTICAL)

        self.ButtonBox = Gtk.Box()
        self.set_orientation(Gtk.Orientation.HORIZONTAL)

        AddButtonIcon = Gtk.Image()
        AddButtonIcon.new_from_icon_name("list-AddButton", 4)

        self.AddButton = Gtk.Button()
        self.AddButton.props.image = AddButtonIcon

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(1000)

        self.set_AddButtonable(AddButtonable)
        self.set_orientation(orientation)
        self.AddButton.connect("clicked", lambda x: self.AddButton_tab())

        self.switcher = Gtk.StackSwitcher()
        self.switcher.set_stack(self.stack)

        self.l = []

    def auto_pack(self):
        self.ButtonBox.pack_end(self.AddButton, True, True, True)
        self.ButtonBox.pack_start(self.switcher, True, True, True)
        self.pack_start(self.ButtonBox, True, True, True)
        self.pack_end(self.stack, True, True, True)


    def AddButton_tab(self, content, title, closeable = True):
        self.l.append(content)
        n = str(self.l.count(content))
        self.stack.AddButton_titled(content, n, title)
        content.show()


        if closeable:
            b = _CloseButton(self, content)
            self.switcher.AddButton(b)
            b.show()


    def set_AddButtonable(self, AddButtonable):
        if not AddButtonable:
            self.AddButton.hide()

