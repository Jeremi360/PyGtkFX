from gi.repository import Gtk


class StandardButton(Gtk.Button):
    def __init__(self, label = "Button", img = Gtk.Image().new_from_icon_name("dialog-information")):
        Gtk.Button.__init__(self)
        self.set_label(label)
        self.set_relief(Gtk.ReliefStyle.NONE)
        self.set_image(img)

class CloseButton(StandardButton):
    def __init__(self):
        self.set_label()
        img = Gtk.Image().new_from_icon_name("dialog-close", 4)
        StandardButton.__init__(self, "Close", img)
        
class HomeButton(StandardButton):
    def __init__(self, label):
        img = Gtk.Image().new_from_icon_name("go-home", 4)
        StandardButton.__init__(self, label, img)
        
class AboutButton(StandardButton):
    def __init__(self):
        img = Gtk.Image().new_from_icon_name("dialog-information", 4)
        StandardButton.__init__(self, "About", img)
        
        
    
