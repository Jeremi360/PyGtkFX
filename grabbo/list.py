from gi.repository import Gtk
import grabbo
import os

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

LIST_UI = os.path.join(r, '..', 'ui', 'List.xml')

class ListElement(grabbo.Builder):
    def __init__(self, label = "Item", element = "item", pylist = ["item"]):
        super(ListElement, self).__init__(LIST_UI)
        self.add = self.ui.get_object("add")
        self.remove = self.ui.get_object("remove")
        self.change = self.ui.get_object("change")
        self.entry = self.ui.get_object("entry")
        self.ok = self.ui.get_object("ok")
        self.cancel = self.ui.get_object("cancel")
        self.change = self.ui.get_object("change")
        self.EditBox = self.ui.get_object("EditBox")
        self.ItemButton = self.ui.get_object("item")
        self.ItemBox = self.ui.get_object("ItemBox")

        self.glist = self.get().parent_instance()
        self.pylist = pylist
        self.element = element
        self.set_label(label)

        self.change.connect("clicked", lambda x: self.on_change())
        self.ok.connect("clicked", lambda x: self.on_ok())
        self.cancel.connect("clicked", lambda x: self.on_cancel())
        self.ItemButton.connect("clicked", lambda x: self.on_item())

        self.add.hide()
        self.EditBox.hide()
        self.ItemBox.show()

    def on_ok(self):
        label = self.entry.get_text()
        self.set_label(label)
        self.show_item()

    def on_cancel(self):
        self.set_label(self.label)
        self.show_item()

    def set_label(self, label):
        self.label = label
        self.ItemButton.set_label(label)
        self.entry.set_text(label)

    def on_change(self):
        self.ItemBox.hide()
        self.EditBox.show()

    def show_item(self):
        self.EditBox.hide()
        self.ItemBox.show()

    def get(self):
        return self.ui.get_object("box")

    def get_index(self):
        i = self.list.index(self.element)
        return i

    def on_item(self):
        i = self.get_index()
        print(self.list[i])

    def on_remove(self):
        self.list.pop(self.get_index())
        self.glist.remove(self.get())




class Window(grabbo.Window):
    def __init__(self):
        super(Window, self).__init__()
        test = ListElement().get()
        self.add(test)
        test.show()
        self.show()


if __name__ == "__main__":
    app = Window()
    Gtk.main()
