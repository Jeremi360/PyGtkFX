from gi.repository import Gtk, Granite
import grabbo
import os

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

LI_UI = os.path.join(r, 'ui', 'ListItem.xml')

class ListItem(grabbo.Builder):
    def __init__(self, label, item, pylist, glist):
        grabbo.Builder.__init__(self, LI_UI)

        self.glist = glist
        self.pylist = pylist
        self.item = item

        self.remove = self.ui.get_object("Remove")
        self.ItemButton = self.ui.get_object("Item")
        self.set_label(label)
        self.EditBox = grabbo.EditBox(self.ItemButton.props.label)

        self.ItemButton.connect("clicked", self.on_item)
        self.remove.connect("clicked", self.on_remove)

    def set_label(self, label):
        self.ItemButton.set_label(label)

    def get(self):
        return self.ui.get_object("box")

    def get_index(self):
        i = self.list.index(self.item)
        return i

    def on_item(self, button):
        i = self.get_index()
        print(self.list[i])

    def on_remove(self, button):
        self.list.pop(self.get_index())
        self.glist.remove(self)

LIST_UI = os.path.join(r, 'ui', 'List.xml')
class List(grabbo.Builder):
    def __init__(self, pylist = []):
        grabbo.Builder.__init__(self, LIST_UI)
        self.LBox = self.ui.get_object("BoxOfList")
        self.CIBox = self.ui.get_object("CurrentItemBox")
        self.FavB = self.ui.get_object("FavButton")
        self.curentItem = None
        self.currentLabel = None

        self.EBCI = grabbo.EditBox(None)

        if pylist != []:
            self.set_pylist(pylist)
        else:
            self.pylist = []

    def set_current(self, label, item):
        self.currentLabel = label
        self.curentItem = item

    def on_fav(self, button):
        if self.FavB.get_state():
            self.add_item(self.currentLabel, self.curentItem)
        else:
            self.remove_item(self.curentItem)

    def add_item(self, label = "LabelOfItem", item = "item"):
        temp = ListItem(label, item, self.pylist, self)
        self.LBox.add(temp.get())
        self.pylist.append(item)

    def remove_item(self, item):
        self.pylist.remove(item)
        self.LBox.remove(item.get())

    def set_pylist(self, pylist):
        self.pylist = pylist
        for i in self.pylist:
            self.add_item(str(i), i)

class Window(grabbo.Window):
    def __init__(self):
        grabbo.Window.__init__(self)
        test = Gtk.Button("Show List")
        self.add(test)
        self.glist = List()
        self.glist.set_pylist(["item1", "item2", "item3"])
        test.connect("clicked", self.on_test)
        test.show()
        self.show()

    def on_test(self, button):
        self.glist.get().show()

if __name__ == "__main__":
    app = Window()
    Gtk.main()
