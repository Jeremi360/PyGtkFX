from gi.repository import Gtk

gtknever = Gtk.PolicyType.NEVER
gtknone = Gtk.ShadowType.NONE
gtkright = Gtk.DirectionType.RIGHT

class NOTEBOOK_UI(Gtk.Box):
    def __init__(self):
        super(NOTEBOOK_UI, self).__init__()
        self.props.hexpand = True
        self.props.vexpand = False

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

        self.ButtonBox = Gtk.Box()
        self.ButtonBox.props.visible = True
        self.ButtonBox.props.can_focus = False
        self.ButtonBox.props.hexpand = True
        self.ButtonBox.props.vexpand = False

        #<property name="expand">True</property>
        #<property name="fill">True</property>

        AddIcon = Gtk.Image()
        AddIcon.new_from_icon_name("list-add", 4)

        self.Add = Gtk.Button()
        self.Add.props.visible = True
        self.Add.props.can_focus = True
        self.Add.props.receives_default = True
        self.Add.props.image = AddIcon
        self.Add.props.relief = gtknone
        self.Add.props.image_position = gtkright

        #<property name="expand">False</property>
        #<property name="fill">False</property>
        #<property name="position">1</property>

        self.pack_end(self.Add, True, True, True)
        self._scrolledwindow.add(self._viewport)
        self.pack_start(self._scrolledwindow, True, True, True)
        self.show_all()

    def add_to_vp(self, children):
        self._viewport.add(children)


class TAB_UI(Gtk.StackSwitcher):
    def __init__(self, stack):
        super(TAB_UI, self).__init__()

