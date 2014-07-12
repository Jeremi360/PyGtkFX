
NOTEBOOK_UI = '''<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.18.3 -->
<interface>
  <requires lib="gtk+" version="3.12"/>
  <object class="GtkImage" id="AddIcon">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="icon_name">list-add</property>
  </object>
  <object class="GtkBox" id="box2">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <child>
      <object class="GtkScrolledWindow" id="scrolledwindow1">
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="vscrollbar_policy">never</property>
        <child>
          <object class="GtkViewport" id="viewport1">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="shadow_type">none</property>
            <child>
              <object class="GtkBox" id="ButtonBox">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <child>
                  <placeholder/>
                </child>
              </object>
            </child>
          </object>
        </child>
      </object>
      <packing>
        <property name="expand">True</property>
        <property name="fill">False</property>
        <property name="position">0</property>
      </packing>
    </child>
    <child>
      <object class="GtkButton" id="Add">
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="receives_default">True</property>
        <property name="image">AddIcon</property>
        <property name="relief">none</property>
        <property name="image_position">right</property>
      </object>
      <packing>
        <property name="expand">False</property>
        <property name="fill">False</property>
        <property name="pack_type">end</property>
        <property name="position">1</property>
      </packing>
    </child>
  </object>
</interface>
'''

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
      <object class="GtkButton" id="TabButton">
        <property name="label" translatable="yes">Tab</property>
        <property name="width_request">5</property>
        <property name="height_request">5</property>
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="receives_default">True</property>
        <property name="valign">start</property>
        <property name="image">TabIcon</property>
        <property name="relief">none</property>
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
        <property name="position">1</property>
      </packing>
    </child>
  </object>
</interface>
'''
