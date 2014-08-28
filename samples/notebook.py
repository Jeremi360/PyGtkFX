from gi.repository import Gtk
import grabbo

class Window(grabbo.Window):
    def __init__(self):
        super(Window, self).__init__()


if __name__ == "__main__":
    app = Window()
    Gtk.main()