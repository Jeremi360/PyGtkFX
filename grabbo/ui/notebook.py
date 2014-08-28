from gi.repository import Gtk

gtknever = Gtk.PolicyType.NEVER
gtknone = Gtk.ShadowType.NONE
gtkright = Gtk.DirectionType.RIGHT

class NOTEBOOK_UI(Gtk.Box):
    def __init__(self):
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
        AddIcon.new_from_icon_name("list-add")

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

        self.pack_end(self.Add)
        self._viewport.add(self.ButtonBox)
        self._scrolledwindow.add(self._viewport)
        self.pack_start(self._scrolledwindow)
        self.show_all()





TAB_UI = '''<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.18.3 -->
<interface>
  <requires lib="gtk+" version="3.10"/>
  <object class="GtkImage" id="CloseIcon">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="icon_name">window-close</property>
  </object>
  <object class="GtkImage" id="TabIcon">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="icon_name">applications-internet</property>
  </object>
  <object class="GtkBox" id="box">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <child>
      <object class="GtkRadioButton" id="TabButton">
        <property name="label" translatable="yes">Tab</property>
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="receives_default">False</property>
        <property name="image">TabIcon</property>
        <property name="xalign">0</property>
        <property name="active">True</property>
        <property name="draw_indicator">False</property>
      </object>
      <packing>
        <property name="expand">False</property>
        <property name="fill">False</property>
        <property name="position">0</property>
      </packing>
    </child>
    <child>
      <object class="GtkButton" id="Close">
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="receives_default">True</property>
        <property name="halign">start</property>
        <property name="valign">start</property>
        <property name="image">CloseIcon</property>
        <property name="relief">none</property>
      </object>
      <packing>
        <property name="expand">False</property>
        <property name="fill">False</property>
        <property name="position">2</property>
      </packing>
    </child>
  </object>
</interface>
'''
