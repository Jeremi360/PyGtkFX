
from gi.repository import Gtk
import grabbo

TBui = grabbo.ui.TAB_UI  #os.path.join('..', 'ui', 'TabButton.ui')
gtknever = Gtk.PolicyType.NEVER
gtknone = Gtk.ShadowType.NONE
gtkright = Gtk.DirectionType.RIGHT

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
    def __init__(self, addable = True, closeable = True, orientation = Gtk.Orientation.HORIZONTAL):
        super(Notebook, self).__init__()
        self.set_orientation(Gtk.Orientation.VERTICAL)

        '''
        self._scrolledwindow = Gtk.ScrolledWindow()
        self._scrolledwindow.props.hexpand = True
        self._scrolledwindow.props.vexpand = False
        self._scrolledwindow.props.vscrollbar_policy = gtknever

        self._viewport = Gtk.Viewport()
        self._viewport.props.visible = True
        self._viewport.props.can_focus = False
        self._viewport.props.hexpand = True
        self._viewport.props.vexpand = False
        self._viewport.props.shadow_type = gtknone
        '''

        self.ButtonBox = Gtk.Box()
        self.set_orientation(Gtk.Orientation.HORIZONTAL)

        AddIcon = Gtk.Image()
        AddIcon.new_from_icon_name("list-add", 4)

        self.Add = Gtk.Button()
        self.Add.props.visible = True
        self.Add.props.can_focus = True
        self.Add.props.receives_default = True
        self.Add.props.image = AddIcon
        self.Add.props.relief = gtknone
        self.Add.props.image_position = gtkright

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(1000)

        self.set_addable(addable)
        self.set_orientation(orientation)
        self.Add.connect("clicked", lambda x: self.add_tab())

        self.switcher = Gtk.StackSwitcher()
        self.switcher.set_stack(self.stack)

        self.ButtonBox.pack_end(self.Add, True, True, True)
        self.ButtonBox.pack_start(self.switcher, True, True, True)
        self.pack_start(self.ButtonBox, True, True, True)
        self.pack_end(self.stack, True, True, True)
        self.l = []
        self.show_all()

    def add_tab(self, content, title, closeable = True):
        self.l.append(content)
        n = str(self.l.count(content))
        self.stack.add_titled(content, n, title)
        content.show()

        if closeable:
            b = _CloseButton(self, content)
            self.switcher.add(b)
            b.show()

    def set_addable(self, addable):
        if not addable:
            self.Add.hide()

