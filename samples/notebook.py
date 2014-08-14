from gi.repository import Gtk
import grabbo

class Window(grabbo.Window):
    def __init__(self):
        super(Window, self).__init__()
        Box = Gtk.VBox()
        N = grabbo.Notebook()
        N.get().show()
        N.pages.show()
        Box.pack_start(N.get(), False, True, 0)
        Box.pack_end(N.pages, True, True, 0)
        self.add(Box)
        Box.show()
        self.show()

if __name__ == "__main__":
    app = Window()
    Gtk.main()