

import gtk, gobject, pango

class Notebook(gtk.Notebook):
    """ TabBase is a generic gtk Notebook object.  If present the return value
    of the widgets get_title and get_icon methods will be used to set the title
    and icon of the tab.  Also if present the widgets close method will 
    determine if the tab should be closed or not unless it is forced to close.
    
    """

    __gproperties__ = {
            'current-page' : (gobject.TYPE_PYOBJECT, 'current page', 
                'the currently active page', gobject.PARAM_READWRITE),
            }

    __gsignals__ = {
            'title-changed' : (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, 
                (gobject.TYPE_STRING,)),
            'exit' : (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, ()),
            'tab-closed' : (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, 
                (gobject.TYPE_PYOBJECT,)),
            'tab-added' : (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, 
                (gobject.TYPE_PYOBJECT,)),
            'new-tab' : (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, 
                (gobject.TYPE_PYOBJECT, gobject.TYPE_PYOBJECT)), 
            }

    def __init__(self, show_tabs=True, action_widget=None):
        """ TabBase(show_tabs=True) -> Initialize the tab settings for the
        notebook.  If 'show_tabs' is True the show the tabs otherwise hide
        them.

        """

        super(Notebook, self).__init__()

        self._current_tab = None
        self._previous_tab = []
        self._switch_new_tab = False
        self._toggle_tabs = not show_tabs

        connection_dict = {
                'page-added': self._page_added_callback,
                'page-removed': self._page_removed_callback,
                'switch-page': self._page_switched_callback,
                'button-press-event': self._tabbar_button_press,
                'button-release-event': self._tabbar_button_release,
                }
        for signal, callback in connection_dict.items():
            self.connect(signal, callback)

        self.set_scrollable(True)
        self.set_show_tabs(show_tabs)
        if action_widget:
            self.set_action_widget(action_widget, gtk.PACK_END)

    def do_get_property(self, prop):
        """ do_get_property(prop) -> Returns the value of custom properties.

        """

        if prop.name == 'current-page':
            return self._current_tab

    def do_set_property(self, prop, value):
        """ do_set_property(prop, value) -> Set the value of properties.

        """

        if prop.name == 'current-page':
            self._current_tab = value

    def toggle_minimize_tab(self, tab=None):
        """ toggle_minimize_tab(tab=None) -> Toggle the visibility of the
        icon of 'tab' or the current tab if 'tab' is None.

        """

        if not tab:
            tab = self._current_tab
        eventbox = self.get_tab_label(tab)
        label = eventbox.get_children()[0].get_children()[-1]
        label.set_property('visible', not label.get_property('visible'))

    def toggle_hide_tab(self, tab=None):
        """ tobble_hide_tab(tab=None) -> Toggle the visibility of the title
        and icon of 'tab,' or the current tab if 'tab' is None.

        """

        if not tab:
            tab = self._current_tab
        eventbox = self.get_tab_label(tab)
        hbox = eventbox.get_children()[0]
        hbox.set_property('visible', not hbox.get_property('visible'))

    def toggle_visible(self, child=None, visible=None):
        """ toggle_visible(child=None, visible=None) -> Toggles the visibility
        of the tab window.  If child is specified it switches to that child
        before showing or instead of hiding (if child is not already focused).
        If visible is not None it us used to override the toggle and force 
        visibility either on or off.

        """

        if not child:
            child = self._current_tab

        if self._current_tab != child:
            self.set_current_page(self.get_children().index(child))
            if visible is None:
                visible = True
        else:
            if visible is None:
                visible = not self.get_property('visible')
        self.set_property('visible', visible)

    def get_current_child(self):
        """ get_current_child -> Return the child of the active tab.

        """

        return self.get_nth_page(self.get_current_page())

    def close_tab(self, child=None, force=False):
        """ close_tab(child=None, force=False) -> Close the tab that 
        contains 'child' or the current tab if child is None.  If force is
        True then remove the tab even if the child does not close.

        """

        if not child:
            child = self._current_tab

        if child not in self.get_children():
            return

        # De-select everything.
        self._grab_clipboard()

        if hasattr(child, 'close') and not force:
            if child.close():
                glib.idle_add(self._close_cleanup, child)
        else:
            glib.idle_add(self._close_cleanup, child)

    def _close_cleanup(self, child):
        """ _close_cleanup(child) -> Do some cleanup before removing and
        destroying 'child.'

        """

        # If the current tab was closed and there were previous tabs, then
        # switch to the last viewed tab in the list.
        if self._current_tab == child and self._previous_tab:
            self.set_current_page(self.page_num(self._previous_tab.pop()))

        # Tell anybody listening that this tab was closed.
        self.emit('tab-closed', child)

        # Remove the tab.
        if child in self.get_children():
            self.remove_page(self.page_num(child))

        # Finally destroy the child of the tab.
        #child.destroy()
        #print('child destroyed')

    def _grab_clipboard(self):
        """ _grab_clipboard() -> Grab the clipboard so the webview can be
        destroyed without causing a segfault.

        """

        # Grab ownership of the clipboard so webkit doesn't segfault.
        clipboard = gtk.clipboard_get('PRIMARY')
        selected_text = clipboard.wait_for_text()
        if selected_text:
            clipboard.set_text(selected_text)
            clipboard.store()

    def new_tab(self, child, switch_to=False):
        """ new_tab(child, switch_to=False) -> Adds a new tab and 
        switches to it if switch_to is True. 
        
        """

        if not switch_to:
            index = self.get_current_page()+1
        else:
            index = -1

        self.add_tab(child, title=child.get_title(), icon=child.get_icon(), 
                index=index, switch_to=switch_to)

    def add_tab(self, child, title, icon=None, index=-1, switch_to=False):
        """ add_tab(child, title, icon=None, index=-1, switch_to=False) ->
        Insert a new tab at 'index' containing 'child.'  Give the new tab 
        a title made from 'title', and 'icon.'  Save the state of 'switch_to.'

        """

        self._switch_new_tab = switch_to
        self.insert_page(child, self.new_tab_label(title, icon=icon), index)

    def new_tab_label(self, title='Blank page', icon=None, max_width=18):
        """ new_tab_label(title='Blank page', icon=None, max_width=18) ->
        Make a new label containing an icon and title.  Make the new label
        'max_width' wide.

        """

        # Set up the label to look nice.
        label = gtk.Label(title)
        label.set_justify(gtk.JUSTIFY_LEFT)
        label.set_alignment(xalign=0, yalign=0.5)
        label.set_width_chars(max_width)
        label.set_max_width_chars(max_width)
        label.set_ellipsize(pango.ELLIPSIZE_END)

        # Add the icon.
        hbox = gtk.HBox(homogeneous=False, spacing=6)
        if not icon:
            icon = gtk.Image()
        hbox.pack_start(icon, False)
        hbox.pack_end(label, True, True)

        eventbox = gtk.EventBox()
        eventbox.add(hbox)
        eventbox.show_all()
        eventbox.set_has_window(False)

        return eventbox

    def set_tab_text(self, child, text):
        """ set_tab_text(child, text) -> Set the text on childs tab label to
        'text.'

        """

        eventbox = self.get_tab_label(child)
        if eventbox:
            eventbox.set_tooltip_text(text)
            eventbox.get_children()[0].get_children()[-1].set_text(text)
            self.set_menu_label_text(child, text)

    def set_tab_icon(self, child, icon):
        """ set_tab_icon(child, icon) -> Set the icon on the childs tab label
        to 'icon.'

        """

        eventbox = self.get_tab_label(child)
        if eventbox:
            tab_icon = eventbox.get_children()[0].get_children()[0]
            self._icon_from_image(icon, tab_icon)

    def set_tab_state(self, tab, state):
        """ set_tab_state(tab, state) -> Set the tab state based on 'state.'
        Minimize the tab if state is 'M', hide the tab if state is 'H', and
        do nothing if state is 'N.'

        """

        if state == 'M':
            self.toggle_minimize_tab(tab)
        elif state == 'H':
            self.toggle_hide_tab(tab)
        else:
            pass

    def get_tab_state(self, tab):
        """ get_tab_state(tab) -> Return the state of the tab.  'M' if the 
        tab is minimized, 'H' if it is hidden, and 'N' if neither.

        """

        try:
            eventbox = self.get_tab_label(tab)
            label = eventbox.get_children()[0].get_children()[-1]
            minimized = not label.get_property('visible')

            hbox = eventbox.get_children()[0]
            hidden = not hbox.get_property('visible')
        except:
            return 'N'

        if hidden:
            return 'H'
        elif minimized:
            return 'M'
        else:
            return 'N'

    def get_tab_icon(self, child):
        """ get_tab_icon(child) -> If the child has a 'get_icon method then 
        use that to get the icon, otherwise use the icon on the tabs label.

        Returns the childs icon or the icon on its tabs label.

        """

        if hasattr(child, 'get_icon'):
            # Just use the icon provided by the tab.
            icon = child.get_icon()
        else:
            # We have to use the icon on the label.
            eventbox = self.get_tab_label(child)
            if eventbox:
                icon = eventbox.get_children()[0].get_children()[0]
        return icon

    def get_tab_text(self, child):
        """ get_tab_text(child) -> Returns the text on the tabs label.

        """

        eventbox = self.get_tab_label(child)
        if eventbox:
            return eventbox.get_children()[0].get_children()[-1].get_text()

    def get_tab_title(self, child):
        """ get_tab_title(child) -> If the child has a 'get_title' method
        use it to get the tabs title, otherwise use its label text.

        Returns the title of 'child', or its tabs label text.

        """

        if hasattr(child, 'get_title'):
            # Good the child provides its own title.
            title = child.get_title()
            if not title:
                title = self.get_tab_text(child)
        else:
            # Grab the tab label instead.
            title = self.get_tab_text(child)
        return title

    def _tab_button_released(self, eventbox, event, child):
        """ _tab_button_released -> When the mouse button is released after
        clicking on a tab either close the tab (if it was middle clicked), or
        popup the menu if it was right clicked.

        """

        if event.button == 2 or \
                (event.button == 1 and event.state & gtk.gdk.CONTROL_MASK):
            # Close the tab on a middle click and control click.
            self.close_tab(child)
        elif event.button == 3:
            # Build the default menu of all the open tabs.
            menu = self._build_popup(clicked_tab=child)

            # Add custom tab items.
            self._add_tab_menu_items(menu, child)
            menu.popup(None, None, None, event.button, event.time, None)

            # We have to return true or the tabbar button release method will
            # execute and we will get two menus.
            return True

    def _tab_button_pressed(self, eventbox, event, child):
        """ _tab_button_pressed -> Called when a mouse button is pressed on
        a tab.  Does nothing right now.

        """

        if event.button == 1 and event.state & gtk.gdk.CONTROL_MASK:
            # Return True so the clicked tab is not raised.
            return True

    def _icon_from_image(self, image, icon):
        """ _icon_from_image(image, icon) -> Set icon to a copy of image.

        """

        image_type = image.get_storage_type()
        if image_type == gtk.IMAGE_PIXBUF:
            icon.set_from_pixbuf(image.get_pixbuf())
        elif image_type == gtk.IMAGE_PIXMAP:
            icon.set_from_pixmap(*image.get_pixmap())
        elif image_type == gtk.IMAGE_ICON_NAME:
            icon.set_from_icon_name(*image.get_icon_name())
        elif image_type == gtk.IMAGE_STOCK:
            icon.set_from_stock(*image.get_stock())
        else:
            icon.set_from_image(*image.get_image())

    def _add_tab_menu_items(self, menu, clicked_tab):
        """ _add_tab_menu_items(menu) -> To be implemented by inheritor. 
        
        """

        pass

    def _build_popup(self, clicked_tab=None):
        """ _build_popup() -> Build the pop up menu.
        
        """

        menu = gtk.Menu()
        
        item_tup = (
                ('_minimize_tab_item', ('gtk-remove', 
                    '_Minimize/Unminimize Tab', True, '<Control>m', 
                    self._minimize_tab_button_released, (clicked_tab,))),
                ('_hide_tab_item', ('view-restore', '_Hide/Unhide Tab', True, 
                    '<Control>h', self._hide_tab_button_released, 
                    (clicked_tab,))),
                gtk.SeparatorMenuItem(),
                )

        accel_group = gtk.AccelGroup()
        menu.set_accel_group(accel_group)

        if clicked_tab:
            for menu_item in item_tup:
                if type(menu_item) == tuple:
                    item_name, (icon_name, label_text, is_sensitive, accel, 
                            clicked_callback, user_args) = menu_item
                    icon = gtk.Image()
                    icon.set_from_icon_name(icon_name, gtk.ICON_SIZE_MENU)
                    item = gtk.ImageMenuItem()
                    item.set_image(icon)
                    item.set_label(label_text)
                    item.set_use_underline(True)
                    item.set_sensitive(is_sensitive)
                    item.connect('button-release-event', clicked_callback, 
                            *user_args)
                    if accel:
                        keyval, modifier = gtk.accelerator_parse(accel)
                        item.add_accelerator('activate', accel_group, keyval, 
                                modifier, gtk.ACCEL_VISIBLE)
                    self.__setattr__(item_name, item)
                else:
                    item = menu_item
                menu.insert(item, item_tup.index(menu_item))

        # Add each tab [icon, title] to menu
        for tab in self.get_children():
            icon = gtk.Image()

            # Get tab icon as image
            self._icon_from_image(self.get_tab_icon(tab), icon)
            text = self.get_tab_title(tab)
            item = gtk.ImageMenuItem()
            item.set_image(icon)
            item.set_label(text)
            label = item.get_children()[0]
            label.set_max_width_chars(48)
            label.set_ellipsize(pango.ELLIPSIZE_END)

            if tab == self._current_tab:
                # Current tab title should be bold italic
                label.modify_font(pango.FontDescription('bold italic'))
            item.connect('button-release-event', 
                    self._popup_item_button_released, tab, menu)
            menu.add(item)
        menu.show_all()

        return menu

    def _minimize_tab_button_released(self, close_tab_item, event, 
            clicked_tab):
        """ _minimize_tab_button_released -> Hide the icon of the clicked tab.

        """

        self.toggle_minimize_tab(clicked_tab)

    def _hide_tab_button_released(self, close_tab_item, event, clicked_tab):
        """ _hide_tab_button_released -> Hide the the label and icon of the 
        clicked tab.

        """
        self.toggle_hide_tab(clicked_tab)

    def _popup_item_button_released(self, item, event, child, menu):
        """ _popup_item_button_released -> Switch to the tab that was
        selected from the popup menu.

        """

        menu.popdown()
        self.set_current_page(self.page_num(child))

    def _page_added_callback(self, tabbar, child, index):
        """ _page_added_callback -> When a page is added make it reorderable,
        and connect to some of its labels signals.  If the switch_new_tab
        variable is True the switch to and grab the focus of the new tab.

        """

        # Get the label and connect to its button press and release events.
        eventbox = self.get_tab_label(child)
        eventbox.connect('button-release-event', self._tab_button_released, 
                child)
        eventbox.connect('button-press-event', self._tab_button_pressed, child)
        self.set_tab_reorderable(child, True)

        # If we are switching to the new page set the input focus to the
        # new child.
        if self._switch_new_tab:
            self.set_current_page(index)
            child.grab_focus()

        # Make the tabs visible if more than one are open.
        if tabbar.get_n_pages() > 1 and self._toggle_tabs:
            self.set_show_tabs(True)

        self.emit('tab-added', child)

    def _page_removed_callback(self, tabbar, child, index):
        """ _page_removed_callback -> Remove the closed tab from the previous
        tab list.  If the last page was closed exit.

        """

        if self.get_n_pages() == 0:
            self.emit('exit')

        # We are not going to need to switch to this tab anymore, so remove
        # it from the list.
        while child in self._previous_tab:
            self._previous_tab.remove(child)

        # Hide the tabs if fewer than one tab is open.
        if tabbar.get_n_pages() < 1 and self._toggle_tabs:
            self.set_show_tabs(False)

    def _page_switched_callback(self, tabbar, page, index):
        """ _page_switched_callback -> After switching to a new tab add the
        previous tab to the previous tab list, and tell anybody listening
        that their title should change.

        """

        # The last tab is the next one in line to switch to when this one is 
        # closed.
        if self._current_tab in self.get_children():
            self._previous_tab.append(self._current_tab)
            if hasattr(self._current_tab, 'active_tab'):
                self._current_tab.active_tab = False

        self.set_property('current-page', self.get_nth_page(index))
        title = self.get_tab_title(self._current_tab)
        self.emit('title-changed', title)

        if hasattr(self._current_tab, 'active_tab'):
            self._current_tab.active_tab = True
            self._current_tab.take_focus()

    def _tabbar_button_press(self, tabbar, event):
        """ _tabbar_button_press -> Open a new tab if the tabbar was double 
        clicked.

        """

        if event.type == gtk.gdk._2BUTTON_PRESS:
            self.emit('new-tab', event.state, self._current_tab)

    def _tabbar_button_release(self, tabbar, event):
        """ _tabbar_button_release -> Popup the tabbar menu if the tabbar was
        right clicked.

        """

        if event.button == 3:
            menu = self._build_popup()
            menu.popup(None, None, None, event.button, event.time, None)
            
win = gtk.Window()
win.connect("destroy", gtk.main_quit)
win.add(Notebook())
win.show_all()
