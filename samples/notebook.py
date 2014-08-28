from gi.repository import Gtk
import grabbo

class Window(grabbo.Window):
    def __init__(self):
        super(Window, self).__init__()

        li = Gtk.Label()
        li.set_label("test 01")

        lii= Gtk.Label()
        lii.set_label("test 02")

        N = grabbo.Notebook()
        N.add_tab(li, li.get_label(), False)
        N.add_tab(lii, lii.get_label(), False)

        hb = Gtk.HeaderBar()
        hb.pack_start(N)
        self.set_titlebar(hb)



if __name__ == "__main__":
    app = Window()
    Gtk.main()