from gi.repository import Gtk
import grabbo

class Window(grabbo.Window):
    def __init__(self):
        super(Window, self).__init__()

        li = Gtk.Label()
        li.set_label("test 01")

        lii= Gtk.Label()
        lii.set_label("test 02")

        s = Gtk.Stack()
        s.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        s.set_transition_duration(1000)

        n = grabbo.Notebook()
        n.set_addable(False)
        n.add_tab(li, "l1", False)
        n.add_tab(lii, "l2", False)

        hb = Gtk.HeaderBar()
        hb.pack_start(n)
        self.set_titlebar(hb)

        n.show()
        self.add(n.stack)
        hb.show_all()
        self.show_all()

if __name__ == "__main__":
    app = Window()
    Gtk.main()