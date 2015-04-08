from gi.repository import Gtk


class StandardButton(Gtk.Button):
    def __init__(self, label, img):
        Gtk.Button.__init__(self)
        self.set_label(label)
        self.set_relief(Gtk.ReliefStyle.NONE)
        self.set_image(img)

class CloseButton(Gtk.Button):
    def __init__(self):
        Gtk.Button.__init__(self)
        self.set_label("Close")
        
        Image = Gtk.Image().new_from_icon_name("dialog-close", 4)
    
